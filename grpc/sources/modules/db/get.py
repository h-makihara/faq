import pymysql.cursors

# 暫定的に今後はこちらへ移行していく
def data(dbTable, col, operator, key, conn):
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {dbTable} WHERE {col} {operator} \"{key}\""
            print('db query is \n %s\n' % query)
            cursor.execute(query)
            result = cursor.fetchall()
    finally:
        return result


# DB から テーブル・プライマリキーの要素と値を指定してデータを取得し返す
def dataFromKey(dbTable, col, key, conn):
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {dbTable} WHERE {col} = \"{key}\""
            print('db query is \n %s\n' % query)
            cursor.execute(query)
            result = cursor.fetchall()
    finally:
        return result

