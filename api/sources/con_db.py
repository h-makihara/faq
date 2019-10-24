import pymysql.cursors

conn = pymysql.connect(
        host='faq_db',
        user='root',
        db='faq',
        password='faq_pass',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )

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
