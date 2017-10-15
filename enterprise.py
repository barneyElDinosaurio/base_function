# coding: utf-8
import json
import requests, time
from lxml import etree

def getdetails():

    headers1 = {'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': 'shop.99114.com',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
                'Cookie': 'shop_login_count=0; Hm_lvt_f160a8c6f9e75fcc0c45d38950c1b318=1505357228; Hm_lpvt_f160a8c6f9e75fcc0c45d38950c1b318=1505359261; _ga=GA1.2.1857728228.1505357228; _gid=GA1.2.1392999576.1505357228',
                'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    headers = {'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': 'shop.99114.com',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive',
               'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
               'Referer': 'http://shop.99114.com/list/area/101119103_2580',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    t = int(time.time())
    t = str(t)
    old = 'shop_login_count=0; Hm_lvt_f160a8c6f9e75fcc0c45d38950c1b318=1505357228; Hm_lpvt_f160a8c6f9e75fcc0c45d38950c1b318=%s; _ga=GA1.2.1857728228.1505357228; _gid=GA1.2.1392999576.1505357228' % t

    cookie_value = {'shop_login_count': '0',
                    'Hm_lvt_f160a8c6f9e75fcc0c45d38950c1b318': '1505357228',
                    'Hm_lpvt_f160a8c6f9e75fcc0c45d38950c1b318': str(t),
                    '_ga': 'GA1.2.1857728228.1505357228',
                    '_gid': 'GA1.2.1392999576.1505357228'}

    temp = json.dumps(cookie_value)
    temp = temp.replace('{', '')
    temp = temp.replace('}', '')
    temp = temp.replace('"', '\'')
    headers['Cookie'] = old
    print headers
    url = 'http://shop.99114.com/list/area/101101_2'

    r = requests.get(url=url, headers=headers1)
    print r.status_code
    print r.text




    header={'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': 'shop.99114.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cookie': 'shop_login_count=0; Hm_lvt_f160a8c6f9e75fcc0c45d38950c1b318=1505357228; Hm_lpvt_f160a8c6f9e75fcc0c45d38950c1b318=1505366980; _ga=GA1.2.1857728228.1505357228; _gid=GA1.2.1392999576.1505357228', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'Referer': 'http://shop.99114.com/', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
    url_1='http://shop.99114.com/list/area/101110105_1'
    r=requests.get(url=url_1,headers=header)
    print r.status_code
    tree=etree.HTML(r.text)
    nodes=tree.xpath('//ul[@class="cony_div"]')
    for node in nodes:
        corps=node.xpath('.//li/a')
        for corp in corps:
            name=corp.xpath('.//strong/text()')[0]
            print name
            link=corp.xpath('.//@href')[0]
            print link

    page_no=tree.xpath('//div[@id="page"]/div/div/form/a/text()')
    print page_no[-2]



def getcity():
    url='http://shop.99114.com/'
    header={'Accept-Language': 'zh,en;q=0.8,en-US;q=0.6', 'Accept-Encoding': 'gzip, deflate', 'Host': 'shop.99114.com', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cookie': 'JSESSIONID=ACFA6B53C8658057203A23A582B9C198; _pk_id.1.0269=4ccae40660a184f5.1508040679.1.1508040679.1508040679.; _pk_ses.1.0269=*; Hm_lvt_07c9269a2ab0c159846a382d09a9a4ac=1508040679; Hm_lpvt_07c9269a2ab0c159846a382d09a9a4ac=1508040679; backUrl="http://web-common.99114.com/siteDubbo/getSiteById?jsonpCallback=jQuery171034474542646050144_1508040678521&_=1508040679110"; siteId=1; _pk_id.100000.0269=f7ca99c1b3599c7f.1508040681.1.1508040681.1508040681.; _pk_ses.100000.0269=*; shop_login_count=0; _ga=GA1.2.92909180.1508040679; _gid=GA1.2.968686470.1508040679; Hm_lvt_f160a8c6f9e75fcc0c45d38950c1b318=1508040679; Hm_lpvt_f160a8c6f9e75fcc0c45d38950c1b318=1508040764', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    content = requests.get(url=url,headers=header).text
    print content


getcity()