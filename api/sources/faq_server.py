from faq_pb2 import *
from faq_pb2_grpc import add_FaqGatewayServicer_to_server, FaqGatewayServicer

from concurrent import futures
from datetime import datetime
import time
import grpc
import con_db

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
                lang = request.faq.lang,
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
        for x in dir(res):
            print(x)
        # temp data for response
        tmp = res.add()
        try:
            # ここでDB接続してデータ取ってくる
            faq_list = con_db.GetData()
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
            tmp.share=faq.get("share")
            tmp.service_name=faq.get("service")
            tmp.lang=faq.get("lang")
            tmp.question=faq.get("question")
            tmp.answer=faq.get("answer")
            print(res)
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
