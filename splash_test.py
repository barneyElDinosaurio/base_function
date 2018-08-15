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
    # headers={''}
    lua_script = """
    function main(splash)
        splash:go(splash.args.url)
        splash:wait(5)
        splash:wait(5)
        return splash:html()
    end
    """
    splash_url = 'http://10.18.6.102:8050/render.html'
    # proxy=get_proxy()
    # url='http://1212.ip138.com/ic.asp'
    # url='https://helloacm.com/api/user-agent/'
    # url='http://www.jsgsj.gov.cn:58888/province/infoQueryServlet.json?pt&c=75B161B67BE862B185C5FBADD913D5BBA5F3EBF07300310A24C11C6EF9F87B0D566A644D16F7111EE62F2388DEF5CA351CBE356AEB9A2326BE613C937889291D'
    # url='http://ssgs.zhuhai.gov.cn/ssdj/ssztkydj0117/201711/t20171116_24906438.htm'
    page=2
    url='http://www.hljcredit.gov.cn/WebCreditQueryService.do?gssearch&type=sxbzxr&detail=true&sxbzxrmc=&proselect=&cityselect=&disselect=&curPageNO={}'.format(page)
    args = {'url':url,'timeout':15,'wait':15,'lua_script':lua_script}
    # args = {'url':url,'timeout':15,'iamges':0,'proxy':proxy}
    # args = {'url':'http://quotes.toscrape.com/js/','timeout':15,'iamge':0}
    response = requests.get(splash_url,params=args)
    # sel = Selector(text=response.text)
    # result = sel.xpath('//div[@class="quote"]/span/text()').extract()
    print(response.text)
    # print(result)

splash_demo()
