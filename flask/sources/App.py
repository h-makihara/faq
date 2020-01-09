from flask_api import FlaskAPI
from . import faq_client
from .protos.faq_pb2 import *
from .protos.faq_pb2_grpc import FaqGatewayStub
import grpc
import json
from google.protobuf.json_format import MessageToJson

app = FlaskAPI(__name__)

@app.route('/hello')
def example():
    return {"hello" : "world"}

@app.route('/faq')
def faqList():
    faqList = []
    with grpc.insecure_channel('faq-grpc:50051') as channel:
        stub = FaqGatewayStub(channel)
        response = faq_client.show_faqs(stub)
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

            print(item.QID)
            print(item.category)
            print(item.scope)
            print(item.service_name)
            print(item.question)
            print(item.answer)
            for tagNum in range(len(item.tag)):
                print(item.tag[tagNum])
        print("faqList is \n\n%s" % faqList)
    return json.dumps(faqList, default=list)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
