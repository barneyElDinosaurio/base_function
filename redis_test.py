# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import redis
r = redis.StrictRedis(host='10.19.133.255', port=6379, db=0)
#print(r.set('zcs','Hello'))
print r.get('zcs')