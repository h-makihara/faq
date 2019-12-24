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

class RouteFaqServicer(FaqGatewayServicer):
    """
    Faqサーバーの実装
    protoで定義したservice名のメソッドを実装する
    """

    faqs = {}

    # TODOを作成するロジック
    def FaqCreate(self, request, response):
        # request.fieldでprotoで定義した値にアクセスできる
        print("Faq Create Called : %s" % request.timestamp)
        try:
            self.faqs[request.faq_name] = FaqComponent(
                qid = request.qid,
                share = request.share,
                service_name = request.service_name,
                category = request.faq.category,
                question = request.faq.question,
                answer = request.faq.answer
                
                # 参考にしたソースのメモなので残す
                # todo_name=request.todo_name,
                # is_done=False    # 作成時はTODO完了していないためFalse
            )
            is_success = True
            message = None
        except:
            import traceback
            traceback.print_exc()
            is_success = False
            message = "something happen"

        # レスポンスを返す時はreturnするだけで良い
        return FaqCreateResponse(
            response=ServerResponseComponent(
                is_success=is_success,
                message=message
            ),
            timestamp=get_timestamp()
        )

    def FaqShow(self, request, response):
        print("Faq Show Called : %s" % request.timestamp)
        faqs = []
        # response data
        res = FaqShowResponse().faq
        # temp data for response
        stream = []
        tmp = res.add()
        try:
            # apiから情報を取得する
            # 将来的に 何をキーにして どう取るか を指定できるようにする
            # gRPC API 同居型
            faq_list = con_db.GetData('tag', 'MAILER-DAEMON')

            # api 分離型の場合
            '''
            api_answer = api.GetData()
            print(api_answer)
            faq_list = api_answer.json()
            '''
            #print(faq_list)
            # これは参考にした元ソース
            #faq_list = [
            #    faq for faq in self.faqs.values()
            #]
        except:
            import traceback
            traceback.print_exc()
            faq_list = []
        # faq_list から不要な情報を削ぐ
        for i in range(len(faq_list)):
            del faq_list[i]['scopeID'], faq_list[i]['serviceID'], faq_list[i]['categoryID']
            print('dropped data is \n%s\n\n' % faq_list[i])
        print('response data is \n%s\n\n\n' % faq_list)
        res = faq_list
        #print('returned response!\n%s\n' % res)
        return FaqShowResponse(faq=res)
        #return FaqShowResponse(faq=res)

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
