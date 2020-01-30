import pymysql.cursors

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

