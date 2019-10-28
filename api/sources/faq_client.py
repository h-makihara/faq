from faq_pb2 import *
from faq_pb2_grpc import FaqGatewayStub
import grpc

from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


# データを送信する関数(関数名は何でもよい)
def create_faq(stub, qid, share, service_name, lang, question, answer):

    # stubにはFaqGatewayが実装されたgRPCサーバーへのアクセス情報が入っている
    # FaqGatewayにはFaqCreateメソッドが実装されているはず
    response = stub.FaqCreate(FaqCreateRequest(
        qid=qid,
        share = share,
        service_name = service_name,
        lang = lang,
        question = question,
        answer = answer
    ))
    #response = stub.FaqCreate(FaqCreateRequest(
    #    faq_name=faq_name,
    #    timestamp=get_timestamp()
    #))

    if response.response.is_success:
        print("create success")
    else:
        print("Error : " + response.response.message)


def show_faqs(stub):
    response = stub.FaqShow(
        FaqShowRequest(
            timestamp=get_timestamp()
        )
    )

    print("---- Faq Name : is done? ----")
    print(response)
    # レスポンスの中のTODOリストにアクセス
    for faq in response.faqs:
        print("%s : %s" % (faq.qid, faq.is_done))

    print("")


def update_faq(stub, faq_name, is_done):
    response = stub.FaqUpdate(
        FaqUpdateRequest(
            faq=FaqComponent(
                faq_name=faq_name,
                is_done=is_done
            ),
            timestamp=get_timestamp()
        )
    )

    if response.response.is_success:
        print("update success")
        if response.response.message:
            print("message : %s" % response.response.message)
    else:
        print("Error : " + response.response.message)

# ここでFAQ ID の最大値を取得し、返す
def getMaxQid():
    return 3

if __name__ == '__main__':

    # localhost:50051にFaqリクエストを送る準備
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = FaqGatewayStub(channel)

        """
        使用方法 : 
            コマンドに従ってstub宛にリクエストを送信する関数を呼び出す
            Faq登録
                c|create [faq_name]
            Faq確認
                s|show
            Faq更新
                u|update [faq_name] [y/n]
        """

        while True:
            command = input().split()
            if len(command) == 0:
                break
            if command[0] == "c" or command[0] == "create":
                # create faq
                qid = getMaxQid() + 1
                try:
                    share = command[1]
                    service_name = command[2]
                    lang = command[3]
                    question = command[4]
                    answer = command[5]
                    #faq_name = command[1]

                except:
                    print("input share range : ", end="")
                    share = input()
                    print("input service_name: ", end="")
                    service_name = input()
                    print("input text lang   : ", end="")
                    lang = input()
                    print("input question    : ", end="")
                    question = input()
                    print("input answer      : ", end="")
                    answer = input()
                create_faq(stub, qid, share, service_name, lang, question, answer)
                #create_faq(stub, faq_name)

            elif command[0] == "s" or command[0] == "show":
                # show faqs
                show_faqs(stub)
            elif command[0] == "u" or command[0] == "update":
                # update faq
                try:
                    qid = command[1]
                    share = command[2]
                    service_name = command[3]
                    lang = command[4]
                    question = command[5]
                    answer = command[6]

                except:
                    print("input qid         : ", end="")
                    qid = input()
                    print("input share range : ", end="")
                    share = input()
                    print("input service_name: ", end="")
                    service_name = input()
                    print("input text lang   : ", end="")
                    lang = input()
                    print("input question    : ", end="")
                    question = input()
                    print("input answer      : ", end="")
                    answer = input()
                update_faq(stub, qid, share, service_name, lang, question, answer)
            else:
                print("input an illigal command, try again.")
