import requests
import time
import simplejson
import setting

def get_proxy(retry=10):
    proxyurl = 'http://{0}/dynamicIp/common/getDynamicIp.do'.format(setting.PROXY)
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
            return proxies_random

p=(print(get_proxy()) for i in range(5))
# print(p)
# for i in p:
#     i
while 1:
    try:
        next(p)
    except Exception as e:
        print(e)
        break
