# -*-coding=utf-8-*-
import json
import re
import requests
import urllib.parse
import config
import time
from fake_useragent import UserAgent
from lxml import etree
from copyheaders import headers_raw_to_dict

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


def parse_header():
    # 替换这个
    header = b'''
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh,en;q=0.9,en-US;q=0.8
    Cache-Control: no-cache
    Connection: keep-alive
    Cookie: _ga=GA1.2.1120330993.1533803771; device_id=45dc0a51a26fc3078e5d8636d5141178; aliyungf_tc=AQAAABUPpRGD+w0AOnFoypiKi1AgLha3; Hm_lvt_1db88642e346389874251b5a1eded6e3=1538060166,1539759418; s=ev17xxecme; _gid=GA1.2.489835841.1540172180; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=0a093a7b60eeaf5abb3468ebb1827ab37492829a; xq_a_token.sig=Ugrl-_BEM5Ed2K1tThP4B9xd-WI; xqat=0a093a7b60eeaf5abb3468ebb1827ab37492829a; xqat.sig=cC3oDwhUgpI-cY_nx4o-fIir8ag; xq_r_token=7147aa65f965bdfd68872710923386e22d547761; xq_r_token.sig=WZ_zkORdsy2K2ngXNlFRV6DkcCg; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=1733473480; u.sig=2sMTnVmBVOASyCZs6lbVBQ6Zfgs; bid=a8ec0ec01035c8be5606c595aed718d4_jnl1zufy; _gat_gtag_UA_16079156_4=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1540258247
    Host: xueqiu.com
    Pragma: no-cache
    Referer: https://xueqiu.com/2227798650/115496801
    User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
    X-Requested-With: XMLHttpRequest
    '''

    header_dict = headers_raw_to_dict(header)
    print(header_dict)
    for k, v in header_dict.items():
        print('"{}":"{}",'.format(str(k, encoding='utf8'), str(v, encoding='utf8')))


def get_proxy(retry=5):
    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
    count = 0
    for i in range(retry):
        try:
            r = requests.get(proxyurl, timeout=3)
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
    s = '李作权与广东省城规建设监理有限公司劳动争议纠纷上诉案'
    headers = getheader()
    base_url = 'https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions={}'
    quote_kw = 'searchWord+{}+1+{}'.format(s, s)
    url = base_url.format(urllib.parse.quote(quote_kw))
    print(url)
    # url='https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord%2B%E6%9D%8E%E4%BD%9C%E6%9D%83%E4%B8%8E%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%9F%8E%E8%A7%84%E5%BB%BA%E8%AE%BE%E7%9B%91%E7%90%86%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8%E5%8A%B3%E5%8A%A8%E4%BA%89%E8%AE%AE%E7%BA%A0%E7%BA%B7%E4%B8%8A%E8'
    # headers['']
    if proxy == False:
        proxies = None
    else:
        proxies = get_proxy()

    r = requests.get(url=url, headers=headers, proxies=proxies)
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

    url = ''
    sub_str = {"excep_tab": "0", "ill_tab": "0", "area": "0", "cStatus": "0", "xzxk": "0", "xzcf": "0",
               "dydj": "0"}

    js_str = json.dumps(sub_str)

    post_data = {
        'conditions': js_str,
        'searchword': '91442000796252026X',
        'sourceType': 'W'

    }

    # 使用json
    r = requests.post(url=url,
                      headers=headers,
                      data=post_data,
                      # json=post_data,
                      # cookies=cookies
                      )
    # r.encoding = 'gbk'
    print(r.text)
    js_data = r.json()

    for item in js_data.get('data').get('result').get('data'):
        print(item)

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
# getheader()
# parse_header()
print(time.ctime())
post_method()
# improve_get_method()
