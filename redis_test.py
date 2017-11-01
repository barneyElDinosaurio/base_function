# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=3)
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
#base_usage()
#insert_data()
#get_data()
#list_usage()
#get_data2()
getMulti()
#get_data2()
getMulti2()