import pymysql.cursors
from . import conn
from . import search
from . import table

def GetData(target, word):
    response = []
    #result = []
    #result = search.fromQID('1', 'JP')
    result = search.fromTag('MAILER-DAEMON')
    table.tableCreate(result)
    conn.close()
    return result

def PutData(faq):
    response = []
    try:
        with conn.cursor() as cursor:
            print("faq is \n%s" % faq)
            # insert faq
            query = "insert into faq(QID,lang,question,answer) VALUES (%s,%s,%s,%s)"
            cursor.execute(query, (faq.QID, faq.lang, faq.question, faq.answer))
            conn.commit()
            # insert basic
            query = "insert into basic(QID,share,service) VALUES(%s,%s,%s)"
            cursor.execute(query, (faq.QID, faq.share, faq.service))
            conn.commit()
    finally:
        table.tableCreate(faq)
        # ここでreturn を書く
        # return 

if __name__=='__main__':
    try:
        with conn.cursor() as cursor:
            # 現在、QIDでのハードコーディングなため1を投げる
            #GetData('QID', 1)
            #result = search.fromQID('1', "JP")
            result = search.fromTag('MAILER-DAEMON')
            #table.tableCreate( result )
    finally:
        conn.close()
