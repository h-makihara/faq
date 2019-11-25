import pymysql.cursors
from . import conn

# DB から テーブル・プライマリキーの要素と値を指定してデータを取得し返す
def dataFromKey(dbTable, col, key):
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {dbTable} WHERE {col} = {key}"
            cursor.execute(query)
            result = cursor.fetchall()    
    finally:
        return result

