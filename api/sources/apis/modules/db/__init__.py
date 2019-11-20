import pymysql.cursors

conn = pymysql.connect(
        host='faq-db',
        user='root',
        db='faq',
        password='faq_pass',
        charset='utf8mb4',
        # Dict型で受け取る
        cursorclass=pymysql.cursors.DictCursor
        )
