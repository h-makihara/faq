import pymysql.cursors
import prettytable

conn = pymysql.connect(
        host='faq_db',
        user='root',
        db='faq',
        password='faq_pass',
        charset='utf8mb4',
        # Dict型で受け取る
        cursorclass=pymysql.cursors.DictCursor
        )

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
            print(result)
            for state in result:
                b_sql = "SELECT share,service FROM basic WHERE QID = %s"
                cursor.execute(b_sql, state.get('QID'))
                b_result = cursor.fetchall()
            i = 0
            for i in range(len(result)):
                result[i].update(b_result[i])
                i += 1

    finally:
        table = prettytable.PrettyTable(["Name", "Value", "type"])
        tableCreate(table,result)
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
        table = prettytable.PrettyTable(["Name", "Value", "type"])
        tableCreate(faq, table)
        # ここでreturn を書く
        # return 

def tableCreate(table, result):
    print("in table create")
    for index in range(len(result)):
        # for logs to prettytable
        table.add_row(
                [
                    "QID",
                    int(result[index].get('QID')),
                    type(int(result[index].get('QID')))
                    ]
                )
        table.add_row(
                [
                    "share",
                    int(result[index].get('share')),
                    type(int(result[index].get('share')))
                    ]
                )
        table.add_row(
                [
                    "s_name",
                    result[index].get('service'),
                    type(result[index].get('service'))
                    ]
                )
        table.add_row(
                [
                    "lang",
                    result[index].get('lang'),
                    type(result[index].get('lang'))
                    ]
                )
        table.add_row(
                [
                    "question",
                    result[index].get('question'),
                    type(result[index].get('question'))
                    ]
                )
        table.add_row(
                [
                    "answer",
                    result[index].get('answer'),
                    type(result[index].get('answer'))
                    ]
                )
    print("response data\n%s" % table)



if __name__=='__main__':
    try:
        with conn.cursor() as cursor:
            sql = "SELECT question,answer FROM faq WHERE answer LIKE %s"
            #sql = "SELECT question,answer FROM faq WHERE qid = %s"
            cursor.execute(sql, ('%大量送信%',))
            result = cursor.fetchall()
            print(result)
    finally:
        conn.close()
