# coding: utf-8
import codecs
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
    #with open('lianjia_body.txt','r') as fp:
    with open('cq_error.txt','r') as fp:
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
        print len(details)
        #print details
        for i in details:
            print i
            print
        #print details[0],details[1],details[2]
        #print price

def get_city_link():
        headers = {'Host': 'm.lianjia.com',
                   'User-Agent': 'UCWEB/2.0 (Linux; U; Adr 2.3; zh-CN; MI-ONEPlus) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile'}
        url = 'https://m.lianjia.com/city/'
        r = requests.get(url=url, headers=headers)
        contnet = r.text
        # print contnet
        tree = etree.HTML(contnet)
        t1 = tree.xpath('//ul[@class="item_lists"]')[1]
        city_list = []
        for city in t1:
            link = city.xpath('.//a/@href')[0]
            if link == '/sh/':
                continue
            if link == '/su/':
                continue
            if link == '/xsbn/':
                continue

            city_list.append('https://m.lianjia.com' + link)
        return city_list

def getXiaoquCount():
        headers= {
            'Host': 'm.lianjia.com',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
            'User-Agent': 'UCWEB/2.0 (Linux; U; Adr 2.3; zh-CN; MI-ONEPlus) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile',
            'X-Requested-With': 'XMLHttpRequest',
            'Cookie':'lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; select_nation=1; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; ubt_load_interval_b=1503971694981; ubta=3154866423.3241223259.1503971686808.1503971686808.1503971695039.2; ubtc=3154866423.3241223259.1503971695041.0EF45810F9672DC3BD68868B080BCCEE; ubtd=2; __xsptplus696=696.1.1503971687.1503971695.2%234%7C%7C%7C%7C%7C%23%23fcZh1fCVH7j7doKzh4kC96wk_XE7Y965%23; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; select_city=510100; gr_session_id_a1a50f141657a94e=1b628432-7a95-4993-91b4-c9d304b67fe6; CNZZDATA1254525948=145009446-1503633660-%7C1503984153; CNZZDATA1253491255=851767322-1503638199-%7C1503987040; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1503987947; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; lianjia_ssid=343c0faf-c443-4673-b900-5c05298bd28a'
            #'Proxy-Authorization': self.authHeader
        }

        city_count={}
        city_link = get_city_link()
        for city in city_link:
            print city
            city_code=city.split('/')[3]
            request_url = city+'xiaoqu/pg1/?_t=1'
            r=requests.get(url=request_url,headers=headers)
            print r
            xiaoqu_count = re.findall(r'\\"total\\":(\d+)}', r.text)[0]
            print "xiaoqu count",xiaoqu_count
            city_count[city_code]=int(xiaoqu_count)
        return city_count

def getSZXiaoqu():
    headers={
        'Host': 'm.lianjia.com',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
        'User-Agent': 'UCWEB/2.0 (Linux; U; Adr 2.3; zh-CN; MI-ONEPlus) U2/1.0.0 UCBrowser/8.6.0.199 U2/1.0.0 Mobile',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie':'lj-ss=5bd2bc45dbdf0644d704777dc2075366; lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; select_nation=1; lj-api=9111950472618e41591b6800072ddacb; _jzqx=1.1504062784.1504062784.1.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/.-; _jzqckmp=1; ubt_load_interval_b=1504076659297; ubta=3154866423.3241223259.1503971686808.1504062380059.1504076659413.19; ubtc=3154866423.3241223259.1504076659416.04775B09D4A0751F8665A61B54987A68; ubtd=19; __xsptplus696=696.5.1504076659.1504076659.1%234%7C%7C%7C%7C%7C%23%230CIWTVwbBidFOpEsVtab9KgnY2MeVIYe%23; select_city=440300; _smt_uid=59a62d3f.3df2aef3; _jzqa=1.1378702697002941000.1504062784.1504062784.1504077919.2; _jzqc=1; _jzqb=1.19.10.1504077919.1; _gat=1; _gat_past=1; _gat_new=1; _gat_global=1; _gat_new_global=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504080215; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; CNZZDATA1254525948=145009446-1503633660-%7C1504076453; CNZZDATA1253491255=851767322-1503638199-%7C1504076896; sample_traffic_test=guide_card; lianjia_ssid=e2c7fbe0-e781-46da-8a9b-29633c6549b5'
    }
    for i in range(300,400):
        access_url='https://m.lianjia.com/sz/xiaoqu/pg%d/?_t=1' %i
        print access_url
        r=requests.get(url=access_url,headers=headers)
        print r.status_code
        parse_body(r.text)

def parse_body(data):
    fp=codecs.open('lianjia_data.txt','a',encoding='utf-8')
    price_month='2017-07'
    crawl_date='2017-08-30'
    js = json.loads(data)
    arg= json.loads(js['args'])
    print "No more data: ",arg['no_more_data']
    body = js['body']
    p = re.compile('"cur_city_name":"(.*?)"')
    city_name = p.findall(js['args'])[0].decode('unicode_escape')
    tree = etree.HTML(body)
    nodes = tree.xpath('//li[@class="pictext"]')
    #log.msg(len(nodes), level=log.INFO)
    print "number: ",len(nodes)
    for node in nodes:
        items = {}
        # xiaoqu_url =node.xpath('.//a[@class="flexbox post_ulog"]/@href')[0]
        # items['xiaoqu_link']=xiaoqu_url
        name = node.xpath('.//div[@class="item_list"]/div[@class="item_main"]/text()')[0]
        items['name'] = name
        desc = node.xpath('.//div[@class="item_list"]/div[@class="item_other text_cut"]/text()')[0]
        items['city_name'] = city_name
        details = desc.split()
        if len(details) == 3:
            # for detail in details:
            items['location'] = details[0]
            items['building_type'] = details[1]
            items['building_date'] = details[2]
        elif len(details) == 2:
            items['location'] = details[0]
            items['building_type'] = "NA"
            items['building_date'] = details[1]
        elif len(details) == 1:
            items['location'] = details[0]
            items['building_type'] = "NA"
            items['building_date'] = 'NA'
        else:
            items['location'] = 'NA'
            items['building_type'] = "NA"
            items['building_date'] = 'NA'
        price_t = node.xpath('.//div[@class="item_list"]/div[@class="item_minor"]/span/em/text()')[0]
        p = re.findall('\d+', price_t)
        if len(p) != 0:
            price = int(price_t)
        else:
            price = '均价未知'
        # items['scrapy_date'] = scrapy_date
        # items['origin']='LJ'
        price_detail = {'price': price, 'origin': 'LJ', 'crawl_date': crawl_date}

        price_list = []
        price_list.append(price_detail)
        price_dict = {price_month: price_list}
        items['price'] = price_dict

        str=json.dumps(items)
        fp.write(str)
        fp.write('\n')

        # print 'type of items : ',type(items)
        #log.msg(items, level=log.INFO)
        #yield items


def getSZXiaoqu_WEB():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
             'Cookie':'lianjia_uuid=c6a7836e-cf96-45ae-96e5-6fdb2def9fb7; UM_distinctid=15e17d9bbf960c-08e33a5d4e4891-4d015463-1fa400-15e17d9bbfa300; gr_user_id=4571568e-96d5-467c-ad95-9dd1f55471e1; select_nation=1; all-lj=6341ae6e32895385b04aae0cf3d794b0; _jzqckmp=1; ubt_load_interval_b=1504076659297; ubta=3154866423.3241223259.1503971686808.1504062380059.1504076659413.19; ubtc=3154866423.3241223259.1504076659416.04775B09D4A0751F8665A61B54987A68; ubtd=19; __xsptplus696=696.5.1504076659.1504076659.1%234%7C%7C%7C%7C%7C%23%230CIWTVwbBidFOpEsVtab9KgnY2MeVIYe%23; select_city=440300; _smt_uid=59a62d3f.3df2aef3; CNZZDATA1255849469=590735468-1504057966-null%7C1504079730; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1503638699; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1504083754; _jzqa=1.1378702697002941000.1504062784.1504077919.1504083754.3; _jzqc=1; _jzqx=1.1504062784.1504083754.2.jzqsr=sz%2Efang%2Elianjia%2Ecom|jzqct=/.jzqsr=sz%2Elianjia%2Ecom|jzqct=/xiaoqu/cro11/; CNZZDATA1254525948=1531358740-1504060252-null%7C1504080168; CNZZDATA1255633284=355134272-1504060008-null%7C1504081609; CNZZDATA1255604082=1601457208-1504060276-null%7C1504081886; _qzja=1.218613373.1504062783783.1504077918805.1504083754402.1504079911341.1504083754402.0.0.0.21.3; _qzjb=1.1504083754402.1.0.0.0; _qzjc=1; _qzjto=21.3.0; _jzqb=1.1.10.1504083754.1; _gat=1; _gat_global=1; _gat_new_global=1; _ga=GA1.2.331020171.1503638699; _gid=GA1.2.2040440312.1503909104; _gat_dianpu_agent=1; lianjia_ssid=e2c7fbe0-e781-46da-8a9b-29633c6549b5'}
    for i in range(1,170):
        url='https://sz.lianjia.com/xiaoqu/pg%dcro21/' %i
        headers['Referer']=url
        r=requests.get(url=url,headers=headers)
        print r.status_code
        parse_lianjia_web(r.text)

def parse_lianjia_web(data):
    fp=open('web_lianjia.txt','a')
    tree=etree.HTML(data)
    nodes=tree.xpath('//ul[@class="listContent"]/li')
    print  "len : ", len(nodes)
    for node in nodes:
        items={}
        name=node.xpath('.//div[@class="title"]/a/text()')[0]
        print name
        items['name']=name
        str1 = json.dumps(items)
        fp.write(str1)
        fp.write('\n')


#getAccess()
#show_body()
#getXiaoquCount()
#getSZXiaoqu()
getSZXiaoqu_WEB()