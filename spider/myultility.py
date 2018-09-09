# -*-coding=utf-8-*-
# @Time : 2018/7/30 11:24
# @File : myultility.py
import re
import config
import requests
import time
from scrapy.selector import Selector

def html_to_text(r):
    p = re.compile('<script.*?</script>', re.S)
    ret = re.sub(p, '', r)
    tree = Selector(text=ret)
    content = tree.xpath('string(.)').extract_first()
    brace_pattern = re.compile('\{.*\}', re.S)
    p2 = re.compile('\r\n', re.S)
    content = re.sub(p2, '', content)
    content = brace_pattern.sub('', content)
    return content

def extract_text(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
                'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Host': 'ssgs.zhuhai.gov.cn',
                'Pragma': 'no-cache', 'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'}
    try:
        r = requests.get(url=url, headers=headers)
    except Exception as e:
        print(e)
    else:
        print('go')
        print(r.status_code)
        r.encoding = 'gb2312'
        content = r.text
        # print(content)
        script_pattern = re.compile('<script .*?</script>', re.S | re.I)
        empty_pattern = re.compile('(\n|\t|\r\n)', re.S | re.I)
        content = script_pattern.sub('', content)

        # tree = etree.HTML(content)
        tree = Selector(text=content)
        content = tree.xpath('string(.)').extract_first()
        # print(content)
        content = empty_pattern.sub('', content)
        print(content)

def download(url, retry=5):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0'}
    for _ in range(retry):
        try:
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                r.encoding = 'utf8'
                return r
            else:
                continue
        except Exception as e:
            print(e)
    return None

def get_proxy(retry=10):
    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
    count = 0
    for i in range(retry):
        try:
            r = requests.get(proxyurl,timeout=3)
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
#
# proxyip = get_proxy()
# print('>>>>proxy ip {}'.format(proxyip))
# while 1:
#     r=requests.get(url='http://httpbin.org/ip',proxies=proxyip)
#     print(r.text)
#     print(time.ctime())
#     time.sleep(1)