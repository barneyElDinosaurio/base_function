# -*-coding=utf-8-*-
# @Time : 2018/7/27 10:21
# @File : extract_text.py
import requests
from lxml import etree
from scrapy.selector import Selector
import re


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

url = 'http://ssgs.zhuhai.gov.cn/ssdj/ssztkydj0117/201604/t20160420_10816006.html'
extract_text(url)
