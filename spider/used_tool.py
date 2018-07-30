# -*-coding=utf-8-*-
# @Time : 2018/7/30 11:24
# @File : used_tool.py
import re

import requests
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