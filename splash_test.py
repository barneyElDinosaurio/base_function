import requests
import time
from scrapy.selector import Selector

def get_proxy(retry=5):
    proxyurl = 'http://120.79.150.101:8081/dynamicIp/common/getDynamicIp.do'
    for i in range(1, retry + 1):
        try:
            r = requests.get(proxyurl, timeout=10)
        except Exception as e:
            print(e)
            print('Failed to get proxy ip, retry ' + str(i))
            time.sleep(1)
        else:
            js = r.json()
            proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
            return proxyServer

def splash_demo():
    headers={''}

    splash_url = 'http://10.18.6.102:8050/render.html'
    proxy=get_proxy()

    # url='http://1212.ip138.com/ic.asp'
    url='https://helloacm.com/api/user-agent/'
    args = {'url':url,'timeout':15,'wait':3,'User-Agent':'FireFox 10.113 IE'}
    # args = {'url':url,'timeout':15,'iamges':0,'proxy':proxy}
    # args = {'url':'http://quotes.toscrape.com/js/','timeout':15,'iamge':0}
    response = requests.get(splash_url,params=args)
    # sel = Selector(text=response.text)
    # result = sel.xpath('//div[@class="quote"]/span/text()').extract()
    print(response.text)
    # print(result)

splash_demo()
