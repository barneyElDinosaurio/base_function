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

def visit_url(url):

    headers = getheader()
    r = requests.get(url=url, headers=headers)
    print(r.text)

# url='https://www.itslaw.com/api/v1/detail?timestamp=1535621066576&judgementId=f2e88e6b-b84c-498d-8499-ecb1152ad5df'
# visit_url(url)

# code_decode()

UA_random()