# coding: utf-8
import requests
from bs4 import BeautifulSoup
from lxml import etree


def xlianjia():
    url='https://m.lianjia.com/sz/xiaoqu/pg5/?_t=1'
    cookie='Cookie:lianjia_uuid=bd5695e2-e708-40ed-a422-bd7735eb0913; UM_distinctid=15dca9b5775ed-0270ab60593b6d-791238-1fa400-15dca9b5776535; _jzqy=1.1502342765.1503554600.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; _jzqckmp=1; select_city=440300; _jzqx=1.1503558036.1503558036.1.jzqsr=sz%2Elianjia%2Ecom|jzqct=/ershoufang/.-; select_nation=1; lj-ss=040f750f334914ad3f62a65590f5df64; _smt_uid=5993d85d.c78ffd9; _jzqa=1.1287000182441332700.1502861406.1503554600.1503558036.4; _jzqc=1; _jzqb=1.5.10.1503558036.1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1502861405,1503378424,1503554600; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503558867; _ga=GA1.2.154142580.1502861407; _gid=GA1.2.332017260.1503554602; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; CNZZDATA1254525948=292510229-1503555399-%7C1503555399; CNZZDATA1253491255=2028382610-1503555874-%7C1503555874; sample_traffic_test=guide_card; lianjia_ssid=81cfa5f2-e251-7036-c82d-d5e9135f7bd3'
    headers={'Accept':'application/json','Host':'m.lianjia.com',
             'User-Agent':'UCWEB/2.0 (Linux; U; Adr 2.3; zh-CN; MI-ONEPlus) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile',
             'X-Requested-With':'XMLHttpRequest'}
    resp=requests.get(url,headers=headers)
    print resp.status_code
    js= resp.json()
    body=js['body']

    tree=etree.HTML(body)

    nodes=tree.xpath('//li[@class="pictext"]')
    for node in nodes:
        name=node.xpath('.//div[@class="item_list"]/div[@class="item_main"]/text()')[0]
        print name
        desc= node.xpath('.//div[@class="item_list"]/div[@class="item_other text_cut"]/text()')[0]
        details=desc.split()
        print len(details)
        for i in  details:
            print i
        price=node.xpath('.//div[@class="item_list"]/div[@class="item_minor"]/span/em/text()')[0]
        print price


lianjia()