# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import redis
# HOSTNAME='raspberrypi'
HOSTNAME='localhost'
r = redis.Redis(host=HOSTNAME, port=6379, db=2)

def base_usage():
    print r.dbsize()
    #r.flushdb()
    print r.dbsize()
    print r.exists('house')
    #r = redis.Redis(host='183.232.57.39', port=7001, db=0,password='jiguang')

    for i in range(10):
        r.set(i,i)
        #每次执行不会覆盖

    for i in range(10):
        x=r.get(i)
        print x
        print type(x)
    #print r.get('test')

#删除数据库
def clear_db(db):
    r=redis.StrictRedis(HOSTNAME,6379,db=db)
    #r.flushdb()
    print r.dbsize()

def insert_data():
    '''
    key='house'
    value=['shenzhen','欧陆经典','2000','160户']
    r.set(key,value)
    '''
    key='dict'
    value={'name':'rocky','age':26,'sex':'f'}
    r.set(key,value)

def get_data():
    keys=r.keys()
    # 返回的事key的列表

    print 'key:',keys,

    for key in keys:
        print key," ",r.get(key),'type ', type(r.get(key))

def list_usage():
    for i in range(10):
        print r.set(i,i*i)

def get_data2():
    k = r.keys()
    for each in k:
        print each
        print r.get(each)
        r.delete(each)

def getMulti():
    d={'a':1,'b' :2,'c':3}
    r.mset(d)

def getMulti2():
    x= r.mget('a','b','c')
    print x

def pop_usage():
    #r.lpush('key',{'hello1':'world'})
    #r.lpush('key','hello')
    #r.lpush('key','hello')
    for i in range(r.llen('key')):
        x= r.lpop('key')
        print type(x)
def get_keys():
    '''
    for i in r.keys():
        print i,
        print r.get(i)
    '''
    print r.llen('codes')
    i=0
    while i<10:
        try:
            x= r.lpop('codes')
            print x
            '''
            d = eval(x[1])
            code = d.keys()[0]
            name = d[d.keys()[0]]
            print code,name
            '''
        except Exception,e:
            print e
            break
        i=i+1
    print "Done"
def check_dup():
    l=r.llen('url')
    print l
    # for i in range(l):
    total = r.lrange('url',0,l)
    for index,i in enumerate(total):
        # print index
        # print i
        pass
    x=len(set(total))
    print x
#base_usage()
#insert_data()
#get_data()
# list_usage()
#get_data2()
#getMulti()
#get_data2()
#getMulti2()
#pop_usage()
#get_keys()
# clear_db(1)
check_dup()