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
    # headers = {'Host': 'www.yzcetc.com', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0',
    #            'Origin': 'http://www.yzcetc.com', 'Upgrade-Insecure-Requests': '1',
    #            'Content-Type': 'application/x-www-form-urlencoded',
    #            'User-Agent': 'Mozilla/5.0AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
    #            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #            'Referer': 'http://www.yzcetc.com/yzcetc/YW_Info/HuiYuanInfo/HuiYuanInfoList.aspx?CategoryNum=004&DanWeiType=13',
    #            'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8'
    #            }

    if 'Content-Length' in headers:
        del headers['Content-Length']
    p = 1

    cookies = {
        'ASP.NET_SessionId': 'ujpxut551fk3sdeh32drst45',
        '__CSRFCOOKIE': '6d3eecf2-7377-45df-b567-b22463f0910f'
    }

    url = 'http://www.yzcetc.com/yzcetc/YW_Info/HuiYuanInfo/HuiYuanInfoList.aspx?CategoryNum=004&DanWeiType=13'

    post_data = {
        '__CSRFTOKEN': '/wEFJDZkM2VlY2YyLTczNzctNDVkZi1iNTY3LWIyMjQ2M2YwOTEwZg==',
        # '__VIEWSTATE': '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',
        '__VIEWSTATE': '',
        '__EVENTTARGET': 'MoreInfoList1$Pager',
        '__EVENTARGUMENT': '60',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': 'crt+WFquap8dbb/rcI5F+HE186Wd1gHjsFizfVvxzZS/UBTVoPgQhqGqNHhaFxWouwxccF2bInfU2TvC4wO7DlYsjnqB3AUyWC7KJk6HgdJeEvZL',
        'MoreInfoList1$txtJSDW': '',
        'MoreInfoList1$txtZZBH': '', }

    # 使用json
    r = requests.post(url=url,
                      headers=headers,
                      # data=post_data,
                      # json=post_data,
                      cookies=cookies
                      )
    r.encoding = 'gbk'
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
    CSRFTOKEN=tree.xpath('//*[@id="__CSRFTOKEN"]/@value')[0]
    VIEWSTATE=tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]

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
# post_method()
improve_get_method()
