# -*-coding=utf-8-*-
import requests
import time
import config

url = 'http://httpbin.org/ip'

def get_proxy(retry=10000):
    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxy_ip)
    count = 0
    for i in range(retry):
        try:
            r = requests.get(proxyurl)
        except Exception as e:
            print(e)
            count += 1
            print('代理获取失败,重试' + str(count))
            time.sleep(1)

        else:
            js = r.json()

            # if len(js.get('port'))<5:
            # print('port number: {}'.format(js.get('port')))
            proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
            proxies_random = {
                'http': proxyServer
            }
            # print(proxies_random)
            return proxies_random
start=time.time()
import json
import datetime
from collections import defaultdict
result = {}
current = datetime.datetime.now()
wait_time = datetime.timedelta(seconds=90)
end_time = current+wait_time
# print(end_time)

# for _ in range(10000000):
#     proxy = get_proxy()
#     s=json.dumps(proxy)
#     result.setdefault(s,0)
#     result[s]=result[s]+1
#     if datetime.datetime.now() > end_time:
#         break
#
#     # print(proxy)
#     # r = requests.get(url,proxies=proxy)
#     # print(r.status_code)
#     # print('web content ::  {}'.format(r.text))
#     # print(proxy)
# # print(result)
#
# print(len(list(result.keys())))
# end = time.time()-start
# print('time used {} ms'.format(end*1000))

import pymongo
db = pymongo.MongoClient('10.18.6.102',port=27018)
doc = db['proxy']['pool']
def mydefine_proxy():
    url='http://api.xdaili.cn/xdaili-api//privateProxy/applyStaticProxy?spiderId={}&returnType=2&count=1'.format(config.spiderid)
    r=requests.get(url)
    print(r.text)
    result=r.json().get('RESULT')
    print(len(result))
    if '提取太频繁' in result:
        return

    proxy_list = r.json().get('RESULT')
    for p in proxy_list:
        print(p)
        current=datetime.datetime.now()
        p['create']=current
        p['work']=True
        doc.insert(p)

def proxy_validate(ip,port):
    proxy='http://{0}:{1}'.format(ip,port)
    try:
        r=requests.get(url='http://httpbin.org/ip',proxies={'http':proxy},timeout=5)
    except Exception as e:
        print(e)
        return False

    if r.json().get('origin')==ip:
        print(ip)
        print('work')
        return True
    else:
        return False

def get_ip_mongo():
    db = pymongo.MongoClient('10.18.6.102',27018)
    docs=db['proxy']['pool']
    for doc in docs.find({'$or':[{"work":True},{"work":None}]}):
        # print(doc)
        ip=doc.get('ip')
        port=doc.get('port')
        if proxy_validate(ip,port):
            docs.update({'ip':ip},{'$set':{'last_update':datetime.datetime.now(),'work':True}})
        else:
            docs.update({'ip':ip},{'$set':{'last_update':datetime.datetime.now(),'work':False}})

# mydefine_proxy()
get_ip_mongo()
