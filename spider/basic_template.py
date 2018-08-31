# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import requests


def getheader():
    # 将header内容拷贝到headers.txt

    with open('headers.txt') as fp:
        data = fp.readlines()
    dictionary = dict()

    for line in data:
        line = line.strip()
        line = line.replace(' ', '')
        dictionary[line.split(":")[0].strip()] = ':'.join(line.split(":")[1:])

    return dictionary


def visit_url(url):

    headers = getheader()
    r = requests.get(url=url, headers=headers)
    print(r.text)

url='https://www.itslaw.com/api/v1/detail?timestamp=1535621066576&judgementId=f2e88e6b-b84c-498d-8499-ecb1152ad5df'
visit_url(url)