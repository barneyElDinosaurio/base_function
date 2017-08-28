# coding: utf-8
import json
import re
import requests
from lxml import etree

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
    'Cookie':'lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; select_city=440300; select_nation=1; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; CNZZDATA1254525948=145009446-1503633660-%7C1503908541; CNZZDATA1253491255=851767322-1503638199-%7C1503907203; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503909560; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; lianjia_ssid=9e199cf4-48f2-4fac-ba8b-bf64c69a5901'
}
def getCityLink():
    fp=open('lianjia_city.txt').read()
    tree=etree.HTML(fp)
    op=open('lianjia_city_link.txt','w')
    for i in tree.xpath('//li/a/@href'):
        print '\'https://m.lianjia.com'+i+'xiaoqu\','
        op.write('https://m.lianjia.com'+i+'xiaoqu'+'\n')


def getCount(url):
    request_url = url + 'pg1/?_t=1'

    r = requests.get(url=request_url, headers=headers)
    print r.text
    xiaoqu_count = re.findall(r'\\"total\\":(\d+)}', r.text)[0]
    print xiaoqu_count

#url='https://m.lianjia.com/hz/xiaoqu/pg1/?_t=1'
#getCount(url)

def getAccess():
    #url='https://m.lianjia.com/sz/xiaoqu'
    url='https://m.lianjia.com/sz/xiaoqu/pg2/?_t=1'
    s=requests.get(url=url,headers=headers)
    print s.text

def show_body():
    with open('lianjia_body.txt','r') as fp:
        content=json.loads(fp.read())['body']
    #print content
    tree=etree.HTML(content)
    nodes=tree.xpath('//li[@class="pictext"]')
    for node in nodes:
        xiaoqu_url = node.xpath('.//a[@class="flexbox post_ulog"]/@href')[0]
        name = node.xpath('.//div[@class="item_list"]/div[@class="item_main"]/text()')[0]
        desc = node.xpath('.//div[@class="item_list"]/div[@class="item_other text_cut"]/text()')[0]
        details = desc.split()
        price = node.xpath('.//div[@class="item_list"]/div[@class="item_minor"]/span/em/text()')[0]
        print xiaoqu_url
        print name
        print details[0],details[1],details[2]
        print price
#getAccess()
show_body()
