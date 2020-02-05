import pymysql.cursors
from . import search
from . import table

def makeConn():
    conn = pymysql.connect(
            host='faq-db',
            user='root',
            db='tmp',
            password='faq_pass',
            charset='utf8mb4',
            # Dict型で受け取る
            cursorclass=pymysql.cursors.DictCursor
            )
    return conn

def GetData(target, word):
    conn = makeConn()
    response = []
    #result = []
    result = search.fromTag(word, conn)
    table.tableCreate(result)
    #conn.close()
    return result

def getFromQID(target, qid):
    conn = makeConn()
    response = []
    result = search.fromQID(qid, 'JP', conn)

    return result[0]

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
