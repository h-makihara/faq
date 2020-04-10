from flask_api import FlaskAPI
from flask import request
from . import faq_client
from .protos.faq_pb2 import *
from .protos.faq_pb2_grpc import FaqGatewayStub
import grpc
import json
from google.protobuf.json_format import MessageToJson

app = FlaskAPI(__name__)


def makeStub():
    with grpc.insecure_channel('faq-grpc:50051') as channel:
        stub = FaqGatewayStub(channel)
    return stub

@app.route('/hello')
def example():
    return {"hello" : "world"}

@app.route('/faq/qa/')
def getqa():
    return "your get request allowed"

@app.route('/faq/qa/<int:qid>', methods=['GET'])
def showFAQ(qid):
    #stub = makeStub()
    qaJson={}
    tags=[]
    with grpc.insecure_channel('faq-grpc:50051') as channel:
        stub = FaqGatewayStub(channel)
        # get qa from grpc server
        response = faq_client.show_qa(stub, qid)
        print(type(response))
        print(response)
        qaJson["QID"]=response.QID
        qaJson["serviceName"]=response.service_name
        qaJson["category"]=response.category
        qaJson["question"]=response.question
        qaJson["answer"]=response.answer
        for tag in response.tag:
            tags.append(tag)
        qaJson["tag"]=tags
    #qaJson = MessageToJson(response)
    print(type(qaJson))
    return json.dumps(qaJson, default=list)
    #return json.dumps(response, default=list)


@app.route('/faq/list')
def faqList():
    word = request.args.get('word', type=str)



    faqList = []


    with grpc.insecure_channel('faq-grpc:50051') as channel:
        stub = FaqGatewayStub(channel)
        # 検索ワードがある場合
        if word is not None:
            print("---\nsearch query is %s\n---\n" % word)
            response = faq_client.search_word(stub, word)
            
        # 検索ワードがない場合、初期アクセスと判断
        else:
            print("---\nword is not set.\ninitial showing...\n---\n")
            response = faq_client.initial_show(stub)
            #response = toJson(faq_client.show_faqs(stub))
        
        print('flask server table printer')
        print(response)
        for item in response:
            faqList.append(
                        {
                            "QID": item.QID, 
                            "category":item.category,
                            "scope":item.scope,
                            "service_name":item.service_name,
                            "question":item.question,
                            "answer":item.answer,
                            "tags":item.tag
                        }
                    )
            # debug
            '''
            print(item.QID)
            print(item.category)
            print(item.scope)
            print(item.service_name)
            print(item.question)
            print(item.answer)
            for tagNum in range(len(item.tag)):
                print(item.tag[tagNum])
        print("faqList is \n\n%s" % faqList)
        '''
        print("faqlist printing...\n\n%s\n\n" % faqList)

    return json.dumps(faqList, default=list)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
