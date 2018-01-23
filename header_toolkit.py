# coding: utf-8
import collections
import datetime
import time

import requests
from lxml import etree


def getheader():
    with open('request_header') as fp:
        data = fp.readlines()
    dictionary = dict()
    for line in data:
        line = line.strip()
        dictionary[line.split(":")[0]] = ':'.join(line.split(":")[1:])
    return dictionary


def analysis_cookie():
    cookie = getheader().get('cookie')
    print cookie
    items = cookie.split(';')
    for item in items:
        name = item.split('=')[0]
        value = item.split('=')[1]
        # print name,value
        name = name.replace(' ', '')
        # print '\'',name,'\'',':','\'',value,'\'',','
        print '\"{}\":\"{}\",'.format(name, value)


def urlParse():
    url = 'http://lg.snssdk.com/api/news/feed/v66/?concern_id=6286225228934679042&refer=1&count=20&max_behot_time=1506210972&last_refresh_sub_entrance_interval=1506220325&loc_mode=0&loc_time=1506071873&latitude=22.552248&longitude=113.903644&city=%E6%B7%B1%E5%9C%B3%E5%B8%82&tt_from=pre_load_more&lac=9365&cid=3672&cp=5493c07313925q1&plugin_enable=3&st_time=333&iid=15189530186&device_id=38220008232&ac=wifi&channel=smartisan&aid=13&app_name=news_article&version_code=636&version_name=6.3.6&device_platform=android&ab_version=179886%2C169863%2C177250%2C179334%2C173967%2C172663%2C172659%2C171194%2C170349%2C178991%2C176179%2C177070%2C169447%2C178210%2C179194%2C168463%2C174398%2C178732%2C178921%2C169300%2C178930%2C180698%2C177166%2C152026%2C176593%2C180172%2C179891%2C178581%2C177786%2C170713%2C179373%2C176739%2C179006%2C156262%2C145585%2C180654%2C179382%2C174429%2C177258%2C180186%2C177042%2C162572%2C176599%2C176609%2C179625%2C175163%2C169176%2C175634%2C176616%2C170988%2C178989%2C176597%2C176652%2C177702%2C176615&ab_client=a1%2Cc4%2Ce1%2Cf2%2Cg2%2Cf7&ab_feature=102749%2C94563&abflag=3&ssmix=a&device_type=SM801&device_brand=SMARTISAN&language=zh&os_api=22&os_version=5.1.1&uuid=990006203070023&openudid=4dd00e258bbe295f&manifest_version_code=636&resolution=1080*1920&dpi=480&update_version_code=6368&_rticket=1506220325881&plugin=2431'
    x = url.split('&')
    fp = open('urlparse', 'w')
    for i in x:
        print i
        fp.write(i + '\n')
    fp.close()


def urlAdd(filename):
    t = int(time.time())
    d = collections.OrderedDict()
    with open(filename, 'r') as fp:
        line = fp.readline().strip()
        url = line
        # print url
        curr_d = datetime.datetime.fromtimestamp(t)
        while 1:
            # print url
            line = fp.readline().strip()
            if len(line) < 1:
                break
            sp = line.split('=')
            print sp[0], " ", sp[1]
            # print sp[0],sp[1]
            # print arg,val
            d[sp[0]] = sp[1]
    base = 'http://lf.snssdk.com/api/news/feed/v66/?concern_id=6286225228934679042'
    # print url
    # r = requests.get(url)
    # print r.json()

    # return url
    # print url
    return d


def read_json():
    fp = open('url', 'r').read().strip()
    # js=json.load(fp,encoding='utf-8')

    # print fp
    # js=json.loads(fp)
    # print js
    return_data = eval(fp)
    print return_data
    # print return_data['log_extra']
    if return_data.has_key('app_name'):
        print return_data.get('app_name')
        print return_data.get('title')
        print return_data.get('image')
        print return_data.get('image').get('url')
        print "TS"

    for k, v in return_data.items():
        # print k,v
        if k == 'image_list':
            # print v
            for i in v:
                for ik, iv in i.items():
                    if ik == 'url_list':
                        picUrl = iv[0].get('url')
                        print picUrl
                        break

        if k == 'filter_words':
            for i in v:
                for k1, v1 in i.items():
                    # print k1,v1
                    pass


def debug_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0',
        'Cookie': 'user-key=ab5c9fb2-b72d-4d11-9da1-e6767d54c55c; cn=45; PCSYCityID=1607; ipLocation=%u5317%u4EAC; areaId=1; ipLoc-djd=1-72-2839-0.295687274; unpl=V2_ZzNtbUUHRUZyW0VWfh5eA2IGGwhKAxATcw4SUnkYXVZlURsNclRCFXwUR1RnGV0UZwEZXEJcQxZFCEdkexhdBGYKFllAVHMldDhFVEsZbAVjAxNZRlJBEnMPRldyGVUHZgsVVUFncxJFDU5ceR9YBVdFRg5BVkIVfDhDXXgcXwdmBhBtQ2dGHHcLQFF5Hl01MW0SXENWQh13AEdSNhlYBWYHFlhAUEUSdQtPVHIbXQ1gCxFtR19LF3MMRmR4; __jdv=122270672|www.yangmaoduo.com|t_1000085532_|tuiguang|6a7b6b234637448d9eb777e7300b3c8a|1515560475236; mt_xid=V2_52007VwMWUlxcVl8dTh9bBWQKEltfWVpdF0opVVdnUxpQCA1OWEhJEUAAZ1AbTlQIUAoDQUsPVmECQgBVClUIL0oYXAx7AhJOXVlDWh1CGFwOZwoiUG1bYl4cTxlZAlcDFlM%3D; _jrda=4; _jrdb=1516031990126; wlfstk_smdl=e9uwhm9b7i6qeg50wp9zgymnutn5kgxy; TrackID=1nOyYSUfe6_U0ZL03hx2fGAyeIiXCymkyAJvixZiNVEKHcCPAyRMNaQJA1NzVCLNDCp8c9u6CW1HJE-xtrKfu56NHOT-k5-s7CjwHhhKxqU8; pinId=hV6bgmIB-TuNeVIABMBRqg; pin=jinweizsu; unick=Rocky-sysu; thor=A5A2F25957E07FA19E4C9149A3AE651FEF9B4B35CF2B77ED096BE087B480D5510426DEA51F1CB32892838B89DB72E1CABCA95D3F86EF35BF74B10E4CD24F26ED6F906A6659D06F697C5AE22C9C7C3016E71EF9CF25FAB3A4826FDCDB3DBBD04EEE3D456AF6D431F0191400E408630EC5CEE0B7FD4F18B09E786E88EC7DCBCA5EEBDF4B956C347379646EBAB80A519E7E; _tp=n6fbtmcC4EgDK0kg5Mk2LQ%3D%3D; _pst=jinweizsu; ceshi3.com=000; __jda=122270672.1510554367612818309692.1510554368.1515742181.1516031886.14; __jdb=122270672.8.1510554367612818309692|14.1516031886; __jdc=122270672; __jdu=1510554367612818309692; 3AB9D23F7A4B3C9B=4CRN6IGHT73R62TD5VBBFGYISFMQCJQM44CBCUGIKUMCKBVWHVAN52JYPYJX5ME6WZFNSGW3QLAEMWB5Y2M2UYRHFM'
    }
    # url = 'https://order.jd.com/center/list.action'
    home_url = 'https://home.jd.com'
    r = requests.get(url=home_url, headers=headers)
    r.encoding = 'utf-8'
    # print r.status_code
    # print type(r.content)
    # print r.text
    # print chardet.detect(r)
    tree = etree.HTML(r.text, parser=etree.HTMLParser(encoding='utf-8'))
    # print etree.tostring(tree)
    print r.text
    return tree, r.text


# 可以随意替换这个header信息
def see_header():
    ua = 'IE'
    header = {'User-Agent': ua}
    r = requests.get(url='https://helloacm.com/api/user-agent/')
    print r.text


print getheader()
# analysis_cookie()
# urlParse()
# read_json()
# print urlAdd('urlparse')
# see_header()
# tree, text = debug_page()
