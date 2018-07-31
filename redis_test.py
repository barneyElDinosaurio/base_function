# -*-coding=utf-8-*-
import redis
import json
# HOSTNAME='raspberrypi'
HOSTNAME = '10.18.6.101'
r = redis.Redis(host=HOSTNAME, port=6379, db=0, decode_responses=True)


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

    for i in range(r.llen('meituan_city_id')):
        ret = r.lindex('meituan_city_id', i)
        print(ret)
        ret_dict = eval(ret)
        print(ret_dict)

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


def get_data():
    # keys = r.keys()
    # 返回的事key的列表
    # print('key:', keys)

    # for key in keys:
    #     print(key, " ", r.get(key), 'type ', type(r.get(key)))

    print(r.llen('hlj0706'))

def list_usage():
    for i in range(10):
        print(r.set(i, i * i))


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
    for i in r.keys():
        print(r.get(i))
        # print(i)
        # print(r.get(i),len(r.get(i)))
        # if len(r.get(i))==0:
        # print(i)


from setting import get_mysql_conn
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

base_usage()
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