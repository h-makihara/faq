import pymysql.cursors

conn = pymysql.connect(
        host='faq_db',
        user='root',
        db='faq',
        password='faq_pass',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )

def GetData():
    try:
        with conn.cursor() as cursor:
            # FaqComponent.faq response
            # a_ is answer sql state
            # b_ is basic sql state
            a_sql = "SELECT * FROM faq WHERE answer LIKE %s"
            #sql = "SELECT question,answer FROM faq WHERE answer LIKE %s"
            #sql = "SELECT question,answer FROM faq WHERE qid = %s"
            cursor.execute(a_sql, ('%大量送信%',))
            a_result = cursor.fetchall()
            print(a_result)
            
            for state in a_result:
                b_sql = "SELECT share,service FROM basic WHERE QID = %s"
                cursor.execute(b_sql, state.get('QID'))
                b_result = cursor.fetchall()
            print(b_result)

    finally:
        conn.close()

    return a_result,b_result

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
