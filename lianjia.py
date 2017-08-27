# coding: utf-8
import re
import requests
from lxml import etree
def getCityLink():
    fp=open('lianjia_city.txt').read()
    tree=etree.HTML(fp)
    op=open('lianjia_city_link.txt','w')
    for i in tree.xpath('//li/a/@href'):
        print '\'https://m.lianjia.com'+i+'xiaoqu\','
        op.write('https://m.lianjia.com'+i+'xiaoqu'+'\n')


def getCount(url):
    request_url = url + 'pg1/?_t=1'
    headers = {
        'Host': 'm.lianjia.com',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'User-Agent': 'UCWEB/2.0 (Linux; U; Adr 2.3; zh-CN; MI-ONEPlus) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile',
        'X-Requested-With': 'XMLHttpRequest',

    }
    r = requests.get(url=request_url, headers=headers)
    print r.text
    xiaoqu_count = re.findall(r'\\"total\\":(\d+)}', r.text)[0]
    print xiaoqu_count

url='https://m.lianjia.com/hz/xiaoqu/pg1/?_t=1'
getCount(url)