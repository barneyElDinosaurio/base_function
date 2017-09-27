# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
import re
import urllib
import hashlib

# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
import pymongo
import requests
import time


def addr_poi(city, addr):
    ak_code = 'pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO'
    addr=city+addr
    queryStr = '/geocoder/v2/?city=%s&address=%s&ret_coordtype=bd09ll&output=json&ak=%s' % (city, addr, ak_code)
    # queryStr = '/geocoder/v2/?address=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO' %addr
    # queryStr='/place/v2/search?q=银河小区&region=杭州市&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO'

    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

    # 在最后直接追加上yoursk
    sk = 'HWMYuBMbfW6sooCmN487953tY495T9vn'
    rawStr = encodedStr + sk
    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
    sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
    url = 'http://api.map.baidu.com/geocoder/v2/?city=%s&address=%s&ret_coordtype=bd09ll&output=json&ak=%s&sn=%s' % (
        city, addr, ak_code, sn)
    s = requests.get(url)
    js = s.json()
    try:
        lng = js['result']['location']['lng']
        lat = js['result']['location']['lat']
    except Exception, e:
        print e
        lng = '0'
        lat = '0'
    return lat, lng


def getcordinate():
    dbname = 'test'
    collection = 'fangtianxia_final1'
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client[dbname]
    data = db[collection].find({'latitude': '0'})
    data_list = list(data)
    print len(data_list)

    for i in range(len(data_list)):
        city = data_list[i]['city_name'].encode('utf-8')
        name = data_list[i]['name'].encode('utf-8')
        print city
        print name
        try:
            lat, lng = addr_poi(city, name)
            print lat, ' , ', lng

            db[collection].update({'name': name, 'city_name': city}, {'$set': {'latitude': lat, 'longitude': lng}},
                                  upsert=True)

            # time.sleep(1)
            print 'done'
        except Exception, e:
            print e
            time.sleep(16)
            continue


def getcordinate_web():
    dbname = 'test'
    collection = 'fangtianxia_url'
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client[dbname]
    data = db[collection].find({'latitude': '0'})
    data_list = list(data)
    headers = {'accept-language': 'zh-CN,zh;q=0.8', 'accept-encoding': 'gzip, deflate, sdch',
               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'upgrade-insecure-requests': '1',
               'cookie': 'global_cookie=i1vd2yl9ur6h23p92d1t7dx4n17j6s78vhh; Integrateactivity=notincludemc; __jsluid=8c5cf9a5eb9efda012120d7d2b59a871; global_wapandm_cookie=m5ncqn52u03eu3yyv3t9rzs4q2hj6ufukec; zhcity=%E6%B7%B1%E5%9C%B3; encity=sz; addr=%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5%9C%B3; newhouse_user_guid=425263D6-787F-4546-0E9F-C2193BEA5A36; newhouse_chat_guid=181C16EB-6981-88DD-71F2-FD20839730CC; unique_cookie=U_l7m5y71pa7e804s0pwjfxtfrs1uj78l1buz*6; JSESSIONID=aaaUBkqzMq4vO9fjTN55v; city=jinzhou; __utmt_t0=1; __utmt_t1=1; __utma=147393320.784965721.1503685036.1505445931.1505453621.18; __utmb=147393320.2.10.1505453621; __utmc=147393320; __utmz=147393320.1504795759.12.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; mencity=gz; unique_wapandm_cookie=U_a5rofalfxrxkrnrt4ma2citfq24j7akkabq*10',
               'pragma': 'no-cache', 'cache-control': 'no-cache',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    for i in range(len(data_list)):
        url = data_list[i]['url']
        print url
        try:
            r = requests.get(url=url, headers=headers)
            print r.status_code
            content = r.text

            position = re.findall('markers=(.*?)&', content)[0]
            longitude = position.split(',')[0]
            latitude = position.split(',')[1]
            print longitude
            print latitude
            db[collection].update({'url': url}, {'$set': {'latitude': latitude, 'longitude': longitude}})
        except Exception, e:
            print e
            print 'fail to get on url', url

        '''
        try:
            lat,lng=addr_poi(city,name)
            print lat,' , ',lng
            db[collection].update({'name': name, 'city_name': city}, {'$set': {'latitude': lat, 'longitude': lng}})
            time.sleep(1)
        except Exception,e:
            print e
            time.sleep(16)
            continue
        '''


if __name__ == '__main__':
    getcordinate()
    # print addr_poi('广州市', '金沙洲建设大道1号')
    # getcordinate_web()
