# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
def base_usage():
    print r.dbsize()
    #r.flushdb()
    print r.dbsize()
    print r.exists('house')
    #r = redis.Redis(host='183.232.57.39', port=7001, db=0,password='jiguang')
    '''
    for i in range(10):
        r.set(i,i)
    
    for i in range(10):
        x=r.get(i)
        print x
        print type(x)
    #print r.get('test')
    '''

def insert_data():
    key='house'
    value=['shenzhen','欧陆经典','2000','160户']
    r.set(key,value)

def get_data():
    keys=r.keys()
    print keys
    for key in keys:
        print r.get(key),'type ', type(r.get(key))

base_usage()
#insert_data()
#get_data()