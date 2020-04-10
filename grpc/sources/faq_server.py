from protos.faq_pb2 import *
from protos.faq_pb2_grpc import add_FaqGatewayServicer_to_server, FaqGatewayServicer

from concurrent import futures
from datetime import datetime
import time
import grpc

# from modules dir
from modules import api
from modules.db import con_db


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def get_timestamp():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def reshapeQA(qa):
    if type(qa) is list:
        print("qa is list data and length is %d" % len(qa))
        print(qa)
        # faq_list から不要な情報を削ぐ
        for i in range(len(qa)):
            del qa[i]['scopeID'], qa[i]['serviceID'], qa[i]['categoryID']
            #qa[i]['createAt'] = qa[i]['createAt'].strftime('%Y/%m/%d')
            print('dropped data is \n%s\n\n' % qa[i])
    elif type(qa) is dict:
        del qa['scopeID'], qa['serviceID'], qa['categoryID']

    return qa

class RouteFaqServicer(FaqGatewayServicer):
    """
    Faqサーバーの実装
    protoで定義したservice名のメソッドを実装する
    """

    faqs = {}

    # 初期表示用関数
    # すべてのデータを取得し、表示する
    def showAll(self, request, response):
        res = faqShowResponse().faq
        # temp data for response
        tmp = res.add()
        try:
            #faq_list = con_db.GetData('tag', 'MAILER-DAEMON')
            faq_list = con_db.GetData('word', 'Mail')

        except:
            import traceback
            traceback.print_exc()
            faq_list = []

        res = reshapeQA(faq_list)
        return faqShowResponse(faq=res)


    # FAQ 一覧を取得するロジック
    #def faqShow(self, request, response):
    def searchWord(self, request, response):
        #print("Faq Show Called : %s" % request.timestamp)
        # response data
        res = multiFaqResponse().faq
        # temp data for response
        tmp = res.add()
        try:
            # apiから情報を取得する
            # 将来的に 何をキーにして どう取るか を指定できるようにする
            # gRPC API 同居型
            #faq_list = con_db.GetData('tag', 'MAILER-DAEMON')
            print("word is %s" % request.word)
            faq_list = con_db.GetData('word', request.word)

            # api 分離型の場合
            '''
            api_answer = api.GetData()
            print(api_answer)
            faq_list = api_answer.json()
            '''
        except:
            import traceback
            traceback.print_exc()
            faq_list = []

        res = reshapeQA(faq_list)
        #print('returned response!\n%s\n' % res)
        return multiFaqResponse(faq=res)

    # QID から QA 情報を取得するロジック
    def showQA(self, request, response):
        res = showQAResponse().faq
        try:
            qa = con_db.getFromQID("JP",request.QID)
            res = reshapeQA(qa)
            """
            res[0]['QID'] = qa.QID
            res[0].scope = qa.scope
            res[0].service_name = qa.service_name
            res[0].category = qa.category
            res[0].question = qa.question
            res[0].answer = qa.answer
            for i in range(len(qa.tag)):
                res[0].tag.append(qa.tag[i])
            """

        except:
            import traceback
            traceback.print_exc()
        print(res)

        return showQAResponse(faq=res)

    def FaqUpdate(self, request, response):
        print("Faq Update Called : %s" % request.timestamp)
        try:
            if request.faq.faq_name in self.faqs:
                message = None
                # 入れ子になっているfieldにもアクセスできる
                self.faqs[request.faq.faq_name].is_done = request.faq.is_done
            else:
                message = "No such a faq"
            is_success = True
        except:
            is_success = False
            message = "something happen"
        return FaqUpdateResponse(
            response=ServerResponseComponent(
                is_success=is_success,
                message=message
            ),
            timestamp=get_timestamp()
        )

# サーバーの実行
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FaqGatewayServicer_to_server(
        RouteFaqServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server Start!!")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
