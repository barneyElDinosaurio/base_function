import requests
import time
import simplejson


def get_proxy():
    proxyurl = 'http://120.79.150.101:8081/dynamicIp/common/getDynamicIp.do'
    count = 0
    while count < 100000:
        try:
            ipreq = requests.get(proxyurl, timeout=10)
            ipcontent = ipreq.content
            ipcontent = simplejson.loads(ipcontent)
            hip = ipcontent['ip']
            hport = ipcontent['port']
            proxyServer = 'http://{0}:{1}'.format(hip, hport)
            # print('   ' + proxyServer)
            proxies_random = {
                'http': proxyServer
            }
            return proxies_random
        except Exception as e:
            print(e)
            count += 1
            print('代理获取失败,重试' + str(count))
            time.sleep(1)


print(get_proxy())
