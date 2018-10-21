# -*-coding=utf-8-*-
import json
import re
import requests
import urllib.parse
import config
import time
from fake_useragent import UserAgent
from lxml import etree

'''
随机user-agent
'''


def UA_random():
    ua = UserAgent()
    print(ua.random)


'''
url编码与解码
urlencode 和 decode
'''


def code_decode():
    content = '%E6%88%90%E9%83%BD'
    uncode_str = urllib.parse.unquote(content)
    print(uncode_str)
    encode_str = urllib.parse.quote(uncode_str)
    print(encode_str)


'''
显示headers
将header内容拷贝到headers.txt
'''


def getheader():
    with open('headers.txt') as fp:
        data = fp.readlines()
    dictionary = dict()

    for line in data:
        line = line.strip()
        line = line.replace(' ', '')
        dictionary[line.split(":")[0].strip()] = ':'.join(line.split(":")[1:])

    print(dictionary)
    return dictionary


def analysis_cookie():
    cookie = getheader().get('Cookie')
    # print(cookie)
    items = cookie.split(';')
    for item in items:
        name = item.split('=')[0]
        value = item.split('=')[1]
        # print(name,value)
        name = name.replace(' ', '')
        # print('\'',name,'\'',':','\'',value,'\'',',')
        print('\"{}\":\"{}\",'.format(name, value))

def get_proxy(retry=5):
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
    return None

def get_method(proxy=False):
    s='李作权与广东省城规建设监理有限公司劳动争议纠纷上诉案'
    headers = getheader()
    base_url='https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions={}'
    quote_kw = 'searchWord+{}+1+{}'.format(s,s)
    url=base_url.format(urllib.parse.quote(quote_kw))
    print(url)
    # url='https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord%2B%E6%9D%8E%E4%BD%9C%E6%9D%83%E4%B8%8E%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%9F%8E%E8%A7%84%E5%BB%BA%E8%AE%BE%E7%9B%91%E7%90%86%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8A%B3%E5%8A%A8%E4%BA%89%E8%AE%AE%E7%BA%A0%E7%BA%B7%E4%B8%8A%E8'
    # headers['']
    if proxy == False:
        proxies = None
    else:
        proxies=get_proxy()

    r = requests.get(url=url, headers=headers,proxies=proxies)
    print(r.text)


def post_method():
    headers = getheader()

    if 'Content-Length' in headers:
        del headers['Content-Length']
    p = 1

    cookies = {
        'ASP.NET_SessionId': 'ujpxut551fk3sdeh32drst45',
        '__CSRFCOOKIE': '6d3eecf2-7377-45df-b567-b22463f0910f'
    }

    url = 'http://122.96.62.234/Wind.WFC.Enterprise.Web/Enterprise/WindSecureApi.aspx?wind.sessionid=75e88a1178c44927a8460685003d4338&cmd=getclassifycompany&page=result-search&s=0.47776212910570837'

    post_data = {
        'pageNo': 0, 'pageSize': 50, 'companyname': '科陆电子',
        'status': '', 'establishedtime': '',
        'feature': '', 'token': '75e88a1178c44927a8460685003d4338',
        'deviceId': 'ffffffff-ccc6-5d51-ffff-ffffe64ecdb1',
        'ver': '1.0.30', 'osName': 'iOS'
    }

    # 使用json
    r = requests.post(url=url,
                      # headers=headers,
                      data=post_data,
                      # json=post_data,
                      # cookies=cookies
                      )
    # r.encoding = 'gbk'
    print(r.text)


# 先访问一页获取某个值
def improve_get_method():
    session = requests.Session()
    headers = getheader()

    if 'Content-Length' in headers:
        del headers['Content-Length']

    r = session.get(url=url,
                    headers=headers)

    # r.encoding = 'gbk'
    tree = etree.HTML(r.text)
    EVENTVALIDATION = tree.xpath('//*[@id="__EVENTVALIDATION"]/@value')[0]
    print(EVENTVALIDATION)
    CSRFTOKEN = tree.xpath('//*[@id="__CSRFTOKEN"]/@value')[0]
    VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]

    # cookies = {
    #     'ASP.NET_SessionId': 'ujpxut551fk3sdeh32drst45',
    #     '__CSRFCOOKIE': '6d3eecf2-7377-45df-b567-b22463f0910f'
    # }

    url = 'http://www.yzcetc.com/yzcetc/YW_Info/HuiYuanInfo/HuiYuanInfoList.aspx?CategoryNum=004&DanWeiType=13'

    post_data = {
        '__CSRFTOKEN': str(CSRFTOKEN),
        '__VIEWSTATE': str(VIEWSTATE),
        '__EVENTTARGET': 'MoreInfoList1$Pager',
        '__EVENTARGUMENT': str(2),
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': str(EVENTVALIDATION),
        'MoreInfoList1$txtJSDW': '',
        'MoreInfoList1$txtZZBH': '',
    }

    # 使用json

    r = session.post(url=url,
                     headers=headers,
                     # data=json.dumps(p),
                     data=post_data,
                     # cookies=cookies
                     )

    r.encoding = 'gbk'
    print(r.text)


# get_method(proxy=True)
# print(getheader())
# code_decode()
# analysis_cookie()
getheader()
# post_method()
# improve_get_method()
