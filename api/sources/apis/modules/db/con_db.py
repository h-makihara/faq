import pymysql.cursors
#import prettytable
from . import conn
from . import table
def GetData(word):
    response = []
    result = []
    try:
        with conn.cursor() as cursor:
            # FaqComponent.faq response
            # a_ is answer sql state
            # b_ is basic sql state
            print("search word is %s" % word)
            a_sql = "SELECT * FROM faq WHERE qid = %s"
            #sql = "SELECT question,answer FROM faq WHERE answer LIKE %s"
            #sql = "SELECT question,answer FROM faq WHERE qid = %s"
            #cursor.execute(a_sql, ('%大量送信%',))
            cursor.execute(a_sql, (word,))
            result = cursor.fetchall()
            # print debug
            #print(result)
            for state in result:
                b_sql = "SELECT share,service FROM basic WHERE QID = %s"
                cursor.execute(b_sql, state.get('QID'))
                b_result = cursor.fetchall()
            i = 0
            for i in range(len(result)):
                result[i].update(b_result[i])
                i += 1

    finally:
        table.tableCreate(result)
        return result
        #conn.close()


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
            GetData(1)
    finally:
        conn.close()
