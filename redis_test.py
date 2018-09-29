# -*-coding=utf-8-*-
import redis
import json
import codecs
import re
from setting import get_mysql_conn
import pymongo
import pandas as pd

HOSTNAME = '10.18.6.102'


def base_usage():
    print(r.dbsize())
    # r.flushdb()
    print(r.dbsize())
    # print(r.exists('house'))
    # r = redis.Redis(host='183.232.57.39', port=7001, db=0,password='jiguang')

    # for i in range(10):
    #     r.set(i, i)
    #     # 每次执行不会覆盖
    #
    # for i in range(10):
    #     x = r.get(i)
    #     print(x)
    #     print(type(x))
    # print(r.get('test'))
    key='meituan_city_id'
    for i in range(10):
        print(r.lpop(key))
    # result = {}
    # for i in range(r.llen(key)):
    #     ret = r.lindex(key, i)
    #     ret=eval(ret)
    #     if ret.get('id') in result:
    #         print(ret.get('id'),ret.get('name'))
    #     else:
    #         result[ret.get('id')]=ret.get('name')

    # print(result)
    # print('done')

# 删除数据库
def clear_db(db):
    r = redis.StrictRedis(HOSTNAME, 6379, db=db)
    # r.flushdb()
    print(r.dbsize())


def insert_data():
    '''
    key='house'
    value=['shenzhen','欧陆经典','2000','160户']
    r.set(key,value)
    '''
    key = 'dict'
    value = {'name': 'rocky', 'age': 26, 'sex': 'f'}
    r.set(key, value)

# 查看某个元素是否在列表里

def get_data():
    pass
    # keys = r.keys()
    # 返回的事key的列表
    # print('key:', keys)

    # for key in keys:
    #     print(key, " ", r.get(key), 'type ', type(r.get(key)))

    # print(r.llen('hlj0706'))


def list_usage():
    l=r.llen('image_url')
    # result_set = set()
    result_list = []
    for i in r.lrange('image_url',0,l):
        # print(r.set(i, i * i))
        result_list.append(i)
    print('list length {}'.format(len(result_list)))
    result_set=list(set(result_list))
    print('set length {}'.format(len(result_set)))

def get_data2():
    k = r.keys()
    for each in k:
        print(each)
        print(r.get(each))
        r.delete(each)


def getMulti():
    d = {'a': 1, 'b': 2, 'c': 3}
    r.mset(d)


def getMulti2():
    x = r.mget('a', 'b', 'c')
    print(x)


def pop_usage():
    for i in range(10):
        r.lpush('mylist', 'Hello')
    # r.lpush('key',{'hello1':'world'})
    # r.lpush('key','hello')
    # r.lpush('key','hello')
    # for i in range(r.llen('mylist')):
    # print(r.lindex('mylist',i))
    # x= r.lpop('key')
    # print(type(x))


def get_keys():
    '''
    for i in r.keys():
        print(i,)
        print(r.get(i))
    '''
    print(r.llen('codes'))
    i = 0
    while i < 10:
        try:
            x = r.lpop('codes')
            print(x)
            '''
            d = eval(x[1])
            code = d.keys()[0]
            name = d[d.keys()[0]]
            print(code,name)
            '''
        except Exception as e:
            print(e)
            break
        i = i + 1


def check_dup():
    l = r.llen('url')
    print(l)
    # for i in range(l):
    total = r.lrange('url', 0, l)
    for index, i in enumerate(total):
        # print(index)
        # print(i)
        pass
    x = len(set(total))
    print(x)


def search():
    r=redis.StrictRedis('10.18.6.102',db=15)
    with codecs.open('remove_test','r','utf8') as f:
        while 1:
            t=f.readline()
            if not t:
                break

            print(r.srem('kjq_name',t.strip()))

    # for i in range(10):
        # if r.sismember('kjq_name','���������������'):
    # print(r.exists('114.230.217.124:38454'))
    # for i in r.keys():
    #     print(r.get(i))
        # print(i)
        # print(r.get(i),len(r.get(i)))
        # if len(r.get(i))==0:
        # print(i)


def convert_sql():
    conn = get_mysql_conn('spider','XGD')
    cur = conn.cursor()

    length = r.llen('hlj0706')
    print(length)
    for i in r.lrange('hlj0706',0,length):
        # print(type(i))
        # print(type(eval(i)))
        d = eval(i)
        name=d.get('name')
        cid=d.get('identify_number')
        cmd ='insert into `tb_hljsxr` (`executed_name`,`cidno`)VALUES ("{}","{}")'.format(name,cid)
        print(cmd)
        try:
            cur.execute(cmd)
            conn.commit()
        except Exception as e:
            print(e)
    conn.close()

# 删除list中某个元素
def remove_item():
    db=pymongo.MongoClient('10.18.6.102',27018)
    doc=db['spider']['ent_history']
    r = redis.Redis(host=HOSTNAME, port=6379, db=11, decode_responses=True)
    location=doc.find({})
    # print('len location {}'.format(len(location)))
    count = 0
    # for item in location:
    #     name=item.get('name')
    #     # print(name)
    #     count +=1
    #     counts=item.get('counts')
    #     crawl_count = item.get('crawl_count')
    #     if crawl_count is None:
    #         print(name)
    #         print(counts)
    #         print(crawl_count)
    #         continue

        # if counts!=crawl_count:
        #     print(name)

        # r.lrem('location',num=1,value=name)
    r.lrem('location',num=1,value='泌阳')
    # for i in range(10):
    #     r.lpush('test',i)
    print(count)

# 删除集合中的某个元素
def remove_set_item():

    r = redis.Redis(host='10.18.6.102', port=6379, db=15, decode_responses=True)
    print(r.srem('kjq_name',''))


def push_excel_redis():
    filename = '失信被执行人爬取关键词.xlsx'
    df = pd.read_excel(filename)
    # print(df.head())
    result = df['行政区划前两字'].values.tolist()
    r = redis.StrictRedis('10.18.6.102', decode_responses=True, db=15)
    for i in result:
        r.lpush('location',i.strip())

# 中文名放到redis

def push_name_redis():
    doc=pymongo.MongoClient('10.18.6.102',port=27018)['db_parker']['kjq_name']
    # r = redis.StrictRedis('10.18.6.102', decode_responses=True, db=15)
    key = 'kjq_name'
    count  = 10000
    current =0
    name_list = []
    with codecs.open(r'E:\temp\CSVFile_2018-09-13T13_20_29\CSVFile_2018-09-13T13_20_29.csv', 'r',encoding='utf8') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            # print(line.strip())
            txt=line.strip()
            ret= re.sub('\s+|[0-9A-Za-z]+|\"|\'|\*|\?|%|&|\.|/|\+|,|;|@|#|�|','',txt)
            print('before {} after {}'.format(txt,ret))
                # continue
            # else:
            if ret:
                name_list.append(ret)
                # r.sadd(key,ret)
                # doc.insert('')

            # if count<current:
            #     break
            # current+=1

            # r.lpush(key, line.strip())
    name_set = list(set(name_list))
    for i in name_set:
        doc.insert({'name':i})

def copy_redis():
    origin = redis.StrictRedis('10.18.4.211', decode_responses=True, db=12)
    destination = redis.StrictRedis('10.18.6.26', decode_responses=True, db=3)
    lens = origin.llen('location_remain')
    for i in origin.lrange('location_remain',0,lens):
        # print(i)
        # print(type(i))
        # try:
        #     x=eval(i).get('name')
        #     destination.sadd('hlj_name',x)
        # except Exception as e:
        #     print(e)
        #     continue
        destination.lpush('location_remain',i)


# base_usage()
# insert_data()
# get_data()
# list_usage()
# get_data2()
# getMulti()
# get_data2()
# getMulti2()
# pop_usage()
# get_keys()
# clear_db(1)
# check_dup()
# search()
# pop_usage()
# convert_sql()
# remove_item()
# push_excel_redis()
# copy_redis()
# push_name_redis()
# search()
# remove_set_item()
copy_redis()