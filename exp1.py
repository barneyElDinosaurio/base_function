import requests
import redis
import time
rds = redis.StrictRedis('localhost',db=5,decode_responses=True)
def get_proxy(retry=10):
    proxyurl = 'http://120.79.150.101:8081/dynamicIp/common/getDynamicIp.do'
    count = 0
    for i in range(retry):
        try:
            r = requests.get(proxyurl, timeout=10)
        except Exception as e:
            print(e)
            count += 1
            print('代理获取失败,重试' + str(count))
            time.sleep(1)
        else:
            js = r.json()
            proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
            print('proxy server {}'.format(proxyServer))
            print('key is',rds.keys())
            if proxyServer in rds.keys():
                print('current proxy: {}'.format(proxyServer))
                continue
            return proxyServer

get_proxy()