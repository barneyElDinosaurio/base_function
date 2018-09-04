# -*-coding=utf-8-*-

# @Time : 2018/9/4 19:57
# @File : myultility.py
import requests
import time


def get_proxy(retry=5):
    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
    for i in range(1, retry + 1):
        try:
            r = requests.get(proxyurl, timeout=2)
        except Exception as e:
            print(e)
            print('Failed to get proxy ip, retry ' + str(i))
            time.sleep(1)
        else:
            js = r.json()
            proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
            return {'http': proxyServer}

    return None