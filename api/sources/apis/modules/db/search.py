import pymysql.cursors
from . import conn
from . import get

# 得た情報からどのように情報を得るかを割り振る機能群
def fromQID(qid, lang):
    # QID からQとAをまず抽出
    # QID からカテゴリを抽出
    # QID からタグを抽出
    # 上記をまとめて return する
    #print('qid is %s, lang is %s' % (qid, lang))
    try:
        with conn.cursor() as cursor:
            query = f"SELECT * FROM {lang} WHERE qid = {qid}"
            cursor.execute(query)
            result = cursor.fetchall()
            #print(result[0].get('scopeID'))
            i = 0
            for i in range(len(result)):
                # get scope
                scopeID = result[i].get('scopeID')
                scope = get.dataFromKey('scope', 'scopeID', scopeID)
                result[i].update(scope[0])

                # get tag
                tagID = get.dataFromKey('tagMap', 'QID', result[i].get('QID'))
                print(tagID)
                tag = get.dataFromKey('tags', 'tagID', tagID[0].get('tagID'))
                print(tag)
                result[i].update(tag[0])
                
                # あと欲しいのは service_name category
                service = get.dataFromKey('services', 'serviceID', result[i].get('serviceID'))
                result[i].update(service[0])
                
                
                # あと欲しいのは category
                categoryID = get.dataFromKey('categoryMap', 'QID', result[i].get('QID'))
                category = get.dataFromKey('categories', 'categoryID', categoryID[0].get('categoryID'))
                result[i].update(category[0])
                print(category)
                print(result[i])
                i += 1
    finally:
        # print is debug data
        return result

def fromCategory(category):
    # category から categoryID を抽出
    # categoryID から Map テーブルよりQID一覧を抽出
    # QID から Q と A を抽出 (fromQID(qid, lang) function)
    # 上記をまとめて return する
    try:
        with conn.cursor() as cursor:
            query = "SELECT category FROM categories WHERE categoryID = %s"
            cursor.execute(query, (category,))
            result = cursor.fetchall()
    finally:
        return result

def fromWord(word, lang):
    # word から QID 一覧を取得
    # QID から tagMap, categoryMap を使ってそれぞれのID取得
    # tagID, categoryID から tag, category を抽出
    # 上記をまとめて return する
    try:
        with conn.cursor() as cursor:
            query = "SELECT category FROM %s WHERE question,answer LIKE %s"
            cursor.execute(query, (lang, word,))
            result = cursor.fetchall()
    finally:
        return result



def fromTag(tag):
    # tag から tagID を取得
    # tagID から tagID を持つ QID を tagMap から抽出
    # QID から Q と A を抽出
    # 上記をまとめて return する
    try:
        with conn.cursor() as cursor:
            query = "SELECT  FROM categories WHERE categoryID = %s"
            cursor.execute(query, (tag,))
            result = cursor.fetchall()
    finally:
        return result

