from protos.faq_pb2 import *
from protos.faq_pb2_grpc import add_FaqGatewayServicer_to_server, FaqGatewayServicer

from concurrent import futures
from datetime import datetime
import time
import grpc
from modules import api

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
        tmp = res.add()
        try:
            # apiから情報を取得する
            # 将来的に 何をキーにして どう取るか を指定できるようにする
            api_answer = api.GetData()
            faq_list = api_answer.json()
            # これは参考にした元ソース
            #faq_list = [
            #    faq for faq in self.faqs.values()
            #]
        except:
            import traceback
            traceback.print_exc()
            faq_list = []

        for faq in faq_list:
            tmp.qid = faq.get("QID")
            tmp.scope=faq.get("scope")
            tmp.service_name=faq.get("service")
            tmp.category=faq.get("category")
            tmp.question=faq.get("question")
            tmp.answer=faq.get("answer")
            # tag は repeated なので for で回して取得
            for tag in faq.get("tag"):
                tmp.tag.append(tag)
        print('returned response!\n%s\n' % res)
        return FaqShowResponse(faq=res)

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
