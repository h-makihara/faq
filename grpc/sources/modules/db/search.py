import pymysql.cursors
from . import con_db
from . import get

# 得た情報からどのように情報を得るかを割り振る機能群
def fromQID(qid, lang, conn):
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
            for i in range(len(result)):
                # get scope
                scopeID = result[i].get('scopeID')
                scope = get.dataFromKey('scope', 'scopeID', scopeID, conn)
                result[i].update(scope[0])

                # get tag
                tags = []
                tagIDs = get.dataFromKey('tagMap', 'QID', result[i].get('QID'), conn)
                j = 0
                for tagID in range(len(tagIDs)):
                    tagData = get.dataFromKey('tags', 'tagID', tagIDs[j].get('tagID'), conn)
                    tags.append(tagData[0].get('tag'))
                    #j += 1
                result[i].update({'tag':tags})

                # あと欲しいのは service_name category
                service = get.dataFromKey('services', 'serviceID', result[i].get('serviceID'), conn)
                result[i].update(service[0])


                # あと欲しいのは category
                categoryID = get.dataFromKey('categoryMap', 'QID', result[i].get('QID'), conn)
                category = get.dataFromKey('categories', 'categoryID', categoryID[0].get('categoryID'), conn)
                result[i].update(category[0])
                #print(result[i])
                #i += 1
    finally:
        # print is debug data
        return result

def fromTag(tag, conn):
    # tag から tagID を取得
    # tagID から tagID を持つ QID を tagMap から抽出
    # QID から Q と A を抽出
    # 上記をまとめて return する
    tagMaps=[]
    tags = get.dataFromKey('tags', 'tag', tag, conn)
    print(len(tags))
    result = []
    # tagID から QID を引く
    for tag in tags:
        tagMaps = get.dataFromKey('tagMap', 'tagID', tag.get('tagID'), conn)
        print('tagMaps is \n%s\n' % tagMaps)
    # QID から残りの情報を取るのは fromQID でできるのでそっちに投げる
    for tagMap in tagMaps:
        print('tagMap is \n%s\n' % tagMap)
        toDict = fromQID(tagMap.get('QID'), 'JP', conn)
        result.append(toDict[0])
        #result.append(fromQID(tagMap.get('QID'), 'JP'))

    return result

def fromCategory(category, conn):
    # category から categoryID を抽出
    # categoryID から Map テーブルよりQID一覧を抽出
    # QID から Q と A を抽出 (fromQID(qid, lang) function)
    # 上記をまとめて return する
    result = []
    category = get.data('categories', 'category', '=', category, conn)
    print(type(category))
    if(category != []):
        try:
            with conn.cursor() as cursor:
                query = "SELECT category FROM categories WHERE categoryID = %s"
                cursor.execute(query, (category,))
                result = cursor.fetchall()
        finally:
            return result

def fromService(word, conn):
    result = []
    services = []
    qids = []
    try:
        services = get.data('services', 'service_name', '=', word, conn)
        for service in services:
            with conn.cursor() as cursor:
                result = get.dataFromKey('JP', 'serviceID', service.get('serviceID'), conn)
                
    finally:
        print("in function result is \n %s \n" % result)
        return result


def fromQA(word, conn):
    qa = get.data('JP', 'CONCAT(answer,question)', 'LIKE', '%'+word+'%', conn)
    return qa

def fromWord(word, lang, conn):
    # word から QID 一覧を取得
    # QID から tagMap, categoryMap を使ってそれぞれのID取得
    # tagID, categoryID から tag, category を抽出
    # 上記をまとめて return する

    # 検索対象 : categories, services, tags, JP

    qids = []
    result = []
    result = fromTag(word, conn)
    if(len(result) > 0):
        for i in range(len(result)):
            qids.append(result[i]['QID'])
    
    result = fromCategory(word, conn)
    if(len(result) > 0):
        for i in range(len(result)):
            qids.append(result[i]['QID'])

    result = fromService(word, conn)
    if(len(result) > 0):
        for i in range(len(result)):
            print("insert data is %s \n" % result[i]['QID'])
            qids.append(result[i]['QID'])
    
    result = fromQA(word, conn)
    if(len(result) > 0):
        for i in range(len(result)):
            qids.append(result[i]['QID'])
    
    
    result.clear()

    for qid in set(qids):
        toDict = fromQID(qid, lang, conn)
        result.append(toDict[0])

    print("get qids is %s\n" % set(qids))
    return result

if __name__ == '__main__':
    conn = con_db.makeConn()
    lang = "JP"
    #word = "MAILER-DAEMON"
    #word = "Mail"
    word = "blog"
    print(fromWord(word, lang, conn))

