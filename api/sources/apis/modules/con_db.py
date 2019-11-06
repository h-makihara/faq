import pymysql.cursors
import prettytable

conn = pymysql.connect(
        host='faq_db',
        user='root',
        db='faq',
        password='faq_pass',
        charset='utf8mb4',
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
            a_sql = "SELECT * FROM faq WHERE answer LIKE %s"
            #sql = "SELECT question,answer FROM faq WHERE answer LIKE %s"
            #sql = "SELECT question,answer FROM faq WHERE qid = %s"
            #cursor.execute(a_sql, ('%大量送信%',))
            cursor.execute(a_sql, ('%'+ word +'%',))
            result = cursor.fetchall()
            
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

        for index in range(len(result)):
            qid = int(result[index].get('QID'))
            share = int(result[index].get('share'))
            s_name = result[index].get('service')
            lang = result[index].get('lang')
            question = result[index].get('question')
            answer = result[index].get('answer')
            
            # for logs to prettytable
            table.add_row(["QID", qid, type(qid)])
            table.add_row(["share", share, type(share)])
            table.add_row(["s_name", s_name, type(s_name)])
            table.add_row(["lang", lang, type(lang)])
            table.add_row(["question", question, type(question)])
            table.add_row(["answer", answer, type(answer)])

        print("response data\n%s" % table)
        return result
        #conn.close()


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
