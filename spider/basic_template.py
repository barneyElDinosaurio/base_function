# -*-coding=utf-8-*-
import json
import re
import requests
import urllib.parse
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


def get_method(url):
    # headers = getheader()
    headers = {'Host': 'www.yzcetc.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
               'Origin': 'http://www.yzcetc.com', 'Upgrade-Insecure-Requests': '1',
               # 'Content-Type': 'application/x-www-form-urlencoded',
               'User-Agent': 'Mozilla/5.0AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
               # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Referer': 'http://www.yzcetc.com/yzcetc/YW_Info/HuiYuanInfo/HuiYuanInfoList.aspx?CategoryNum=004&DanWeiType=13',
               'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8'
               }

    r = requests.get(url=url, headers=headers)
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

    url = 'http://oa.xinguodu.com/login/VerifyLogin.jsp'

    post_data = {
        'loginfile': '/wui/theme/ecology7/page/login.jsp?templateId=4&logintype=1&gopage=',
        'logintype': '1',
        'fontName': '微软雅黑',
        'message': '',
        'gopage': '',
        'formmethod': 'post',
        'rnd': '',
        'serial': '',
        'username': '',
        'isie': 'false',
        'loginid': 'wangshuai',
        'userpassword': 'cjw@0619',
        'submit': '',
    }

    # 使用json
    r = requests.post(url=url,
                      headers=headers,
                      data=post_data,
                      # json=post_data,
                      cookies=cookies
                      )
    # r.encoding = 'gbk'
    print(r.text)



# 先访问一页获取某个值
def improve_get_method():
    session = requests.Session()
    headers = getheader()

    if 'Content-Length' in headers:
        del headers['Content-Length']

    url = 'http://www.yzcetc.com/yzcetc/YW_Info/HuiYuanInfo/HuiYuanInfoList.aspx?CategoryNum=004&DanWeiType=13'

    r = session.get(url=url,
                    headers=headers)

    r.encoding = 'gbk'
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


# url='https://weibo.cn/search/mblog?hideSearchFrame=&keyword=000001&page=1'
# url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信被执行人名单&cardNum=&iname=峨眉&areaName=&pn=10&rn=10&ie=utf-8&oe=utf-8&format=json&t=1536300591664&cb=jQuery1102018043360291625454_1536300402086&_=1536300402101'
# get_method(url)
# print(getheader())
# code_decode()
# analysis_cookie()
# getheader()
post_method()
# improve_get_method()
