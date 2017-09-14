# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
import urllib
import hashlib

# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
import pymongo
import requests
import time


def addr_poi(city,addr):
    queryStr = '/geocoder/v2/?city=%s&address=%s&ret_coordtype=bd09ll&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO' %(city,addr)
    #queryStr = '/geocoder/v2/?address=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO' %addr
    #queryStr='/place/v2/search?q=银河小区&region=杭州市&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO'

    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

    # 在最后直接追加上yoursk
    rawStr = encodedStr + 'HWMYuBMbfW6sooCmN487953tY495T9vn'
    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
    sn= hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
    url='http://api.map.baidu.com/geocoder/v2/?city=%s&address=%s&ret_coordtype=bd09ll&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&sn=%s' %(city,addr,sn)
    s=requests.get(url)
    js=s.json()
    try:
        lng= js['result']['location']['lng']
        lat= js['result']['location']['lat']
    except Exception,e:
        print e
        lng='0'
        lat='0'
    return lat,lng

def getcordinate():
    dbname='test'
    collection='fangtianxia_drop_dup'
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db=client[dbname]
    data=db[collection].find({'latitude':{'$exists':False}})
    data_list=list(data)
    for i in range(len(data_list)):
        city=data_list[i]['city_name'].encode('utf-8')
        name=data_list[i]['name'].encode('utf-8')
        print city
        print name
        try:
            lat,lng=addr_poi(city,name)
            print lat,' , ',lng
            db[collection].update({'name': name, 'city_name': city}, {'$set': {'latitude': lat, 'longitude': lng}})
        except Exception,e:
            print e
            time.sleep(16)
            continue

if __name__=='__main__':
    getcordinate()