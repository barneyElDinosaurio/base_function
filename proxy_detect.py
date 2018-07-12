# -*-coding=utf-8-*-
import requests
import time

url = 'http://members.3322.org/dyndns/getip'


def get_proxy(retry=5):
    proxyurl = 'http://:8081/dynamicIp/common/getDynamicIp.do'
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
            proxies_random = {
                'http': proxyServer
            }
            print(proxies_random)
            return proxies_random

proxy = get_proxy()
r = requests.get(url,proxies=proxy)
print('web content {}'.format(r.text))