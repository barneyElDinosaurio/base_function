# -*-coding=utf-8-*-
# @Time : 2018/8/16 13:35
# @File : hjl_mine.py
import requests
import time
from lxml import etree


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
            proxy_server = {'http': 'http://{}:{}'.format(js.get('ip'), js.get('port'))}
            # proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
            return proxy_server
    return None


session = requests.Session()
page = 3
headers = {'User-Agent': 'Fox 4.3'}
proxy = get_proxy()
home = 'http://www.hljcredit.gov.cn/WebCreditQueryService.do?gssearch&type=sxbzxrqg&detail=true&sxbzxrmc=&proselect=&cityselect=&disselect=&curPageNO={}'.format(
    page)
# s = session.get(url=home,headers=headers)
s = session.get(url=home, headers=headers, proxies=proxy)
print(s.status_code)
# print(s.text)
tree = etree.HTML(s.text)
for url in tree.xpath('//table[@class="list_2_tab"]/tr/td/a/@href'):
    # next_url  = tree.xpath('//table[@class="list_2_tab"]/tr[2]/td[2]/a/@href')[0]
    details = 'http://www.hljcredit.gov.cn/' + url
    # proxy=get_proxy()

    s2 = session.get(details, headers=headers, proxies=proxy)
    # s2=session.get(details,headers=headers)
    # print(s2.text)
    detail_tree = etree.HTML(s2.text)
    print(detail_tree.xpath('//table[@class="for_letter"]/tr[2]/td[2]/text()')[0])
