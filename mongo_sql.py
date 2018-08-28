# -*-coding=utf-8-*-
import pandas as pd
import json
import pymongo
# from setting import get_engine
from sqlalchemy import create_engine

# 将mongo数据转移到mysql

client = pymongo.MongoClient('10.18.6.101')
doc = client['spider']['meituan']
<<<<<<< HEAD
# engine = get_engine('')
engine = create_engine('mysql+pymysql://crawler:Crawler@1234@10.18.4.211:3367/spider?charset=utf8')
=======
engine = create_engine('mysql+pymysql://:@1234@10.18.4.211:/spider?charset=utf8')
>>>>>>> origin/master


def classic_method():
    temp = []
    start = 0
    # 数据太大还是会爆内存,或者游标丢失
<<<<<<< HEAD
=======

>>>>>>> origin/master
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
    block = 10000
    total = doc.find({}).count()
    iter_number = total // block
<<<<<<< HEAD
    # remain_part = total%block
=======

>>>>>>> origin/master
    for i in range(iter_number + 1):
        small_part = doc.find({}).limit(block).skip(i * block)
        list_data = []

        for item in small_part:
            del item['_id']
            del item['crawl_time']
            item['poiid'] = int(item['poiid'])
            for k, v in item.items():
                if isinstance(v, dict) or isinstance(v, list):
<<<<<<< HEAD
                    # print(v)
                    item[k] = json.dumps(v, ensure_ascii=False)
                # else:
                # print(v)
=======

                    item[k] = json.dumps(v, ensure_ascii=False)

>>>>>>> origin/master
            list_data.append(item)

        df = pd.DataFrame(list_data)
        df = df.set_index('poiid', drop=True)
<<<<<<< HEAD
        # print(df.head(5))

        try:
            # pass
=======

        try:
>>>>>>> origin/master
            df.to_sql('meituan', con=engine, if_exists='append')
            print('to sql {}'.format(i))
        except Exception as e:
            print(e)

<<<<<<< HEAD

chunksize_move()

=======
chunksize_move()
>>>>>>> origin/master
