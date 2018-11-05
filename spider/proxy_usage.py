import requests
import time
import simplejson
import setting
import config
def get_proxy(retry=10):
    count=0
    proxyurl = 'http://:8081/dynamicIp/common/getDynamicIp.do'
    for i in range(retry):
        try:
            r = requests.get(proxyurl, timeout=10)
            print(r.text)
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

# p=(print(get_proxy()) for i in range(5))
# # print(p)
# # for i in p:
# #     i
# while 1:
#     try:
#         next(p)
#     except Exception as e:
#         print(e)
#         break

def get_binhttp():
    proxy=get_proxy()
    print(proxy)
    r = requests.get(
        url='http://httpbin.org/ip',
        proxies=proxy
    )

    print(r.text)
    print(r.json())

get_binhttp()


