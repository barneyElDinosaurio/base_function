# -*-coding=utf-8-*-
import pandas as pd
import json
import pymongo
from sqlalchemy import create_engine
import config
# 将mongo数据转移到mysql

client = pymongo.MongoClient('10.18.6.102')
doc = client['stock']['jsl']
engine = create_engine('mysql+pymysql://root:123456z@127.0.0.1:3306/db_rocky?charset=utf8'.format(config.localpassword))


def classic_method():
    temp = []
    start = 0
    # 数据太大还是会爆内存,或者游标丢失

    for i in doc.find().batch_size(500):
        start += 1
        del i['_id']
        temp.append(i)
        print(start)

    print('start to save to mysql')
    df = pd.read_json(json.dumps(temp))
    df = df.set_index('poiid', drop=True)
    df.to_sql('meituan', con=engine, if_exists='replace')
    print('done')


def chunksize_move():
    block = 100
    total = doc.find({}).count()
    iter_number = total // block

    # remain_part = total%block

    for i in range(iter_number + 1):
        small_part = doc.find({}).limit(block).skip(i * block)
        list_data = []

        for item in small_part:
            del item['_id']
            # del item['crawl_time']
            item['poiid'] = int(item['poiid'])
            for k, v in item.items():
                if isinstance(v, dict) or isinstance(v, list):

                    # print(v)
                    item[k] = json.dumps(v, ensure_ascii=False)
                # else:
                # print(v)


                    item[k] = json.dumps(v, ensure_ascii=False)


            list_data.append(item)
        df = pd.DataFrame(list_data)
        df = df.set_index('poiid', drop=True)
        # print(df.head(5))

        try:
            df.to_sql('meituan', con=engine, if_exists='append')
            print('to sql {}'.format(i))
        except Exception as e:
            print(e)

def mongo_transfer():
    doc = client['stock']['jsl']
    backup_mongo=pymongo.MongoClient('10.18.6.101')['stock']['jsl']
    block = 100
    total = doc.find({}).count()
    iter_number = total // block

    for i in range(iter_number + 1):
        small_part = doc.find({}).limit(block).skip(i * block)
        # list_data = []
        for item in small_part:
            print('insert.....')
            backup_mongo.insert(item)

    print('done')

# chunksize_move()
mongo_transfer()
