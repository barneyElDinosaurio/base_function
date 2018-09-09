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
            print(proxies_random)
            return proxies_random
start=time.time()
for _ in range(10):
    proxy = get_proxy()
    print(proxy)
    r = requests.get(url,proxies=proxy)
    print(r.status_code)
    print('web content ::  {}'.format(r.text))
    print(proxy)
end = time.time()-start
print('time used {} ms'.format(end*1000))