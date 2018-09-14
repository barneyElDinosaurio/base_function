# -*-coding=utf-8-*-

import requests
import urllib.parse
from fake_useragent import UserAgent

'''
随机user-agent
'''
def UA_random():
    ua=UserAgent()
    print(ua.random)

'''
url编码与解码
 urlencode 和 decode
'''

def code_decode():

    content = 'http://www.bidchance.com/info.do?channel=biangeng&id=5672342&q=%D5%D0%C9%CC'
    # content = '%E6%88%90%E9%83%BD'
    uncode_str = urllib.parse.unquote(content)
    print(uncode_str)
    # encode_str = urllib.parse.quote(uncode_str)
    # print(encode_str)

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

def visit_url(url):

    headers = getheader()
    r = requests.get(url=url, headers=headers)
    print(r.text)

url='http://ggzy.yazw.gov.cn:8016/JyWeb/XXGK/ZhongJieFuWuChaXunGetList?PageIndex=3&PageSize=15&ZiZhiLeiBieGuid=1c94d458-3a98-410a-8f2b-89360edb311e&isZhongXuan=False&X-Requested-With=XMLHttpRequest'
# url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=失信被执行人名单&cardNum=&iname=峨眉&areaName=&pn=10&rn=10&ie=utf-8&oe=utf-8&format=json&t=1536300591664&cb=jQuery1102018043360291625454_1536300402086&_=1536300402101'
# visit_url(url)
print(getheader())
# code_decode()