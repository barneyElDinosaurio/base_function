# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
import random
import urllib
import hashlib

# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
import pymongo
import requests
import time


def getcordinate():

    client = pymongo.MongoClient('127.0.0.1', 27017)
    db=client.test
    data=db.total_lianjia_copy.find({'city_name':'东莞'},{'name':1,'city_name':1})
    data_list=list(data)
    for i in range(len(data_list)):
        city= data_list[i]['city_name'].encode('utf-8')
        addr= data_list[i]['name'].encode('utf-8')

        #print type(city)
        #print type(addr)
        #city='上海'
        #addr='学府花苑'
        queryStr = '/geocoder/v2/?address=%s&city=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO' %(addr,city)
        print queryStr
        # 对queryStr进行转码，safe内的保留字符不转换
        encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

        # 在最后直接追加上yoursk
        rawStr = encodedStr + 'HWMYuBMbfW6sooCmN487953tY495T9vn'

        # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
        # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
        sn= hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
        #print sn
        url='http://api.map.baidu.com/geocoder/v2/?address=%s&city=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&sn=%s' %(addr,city,sn)
        s=requests.get(url)
        try:
            js=s.json()
        #print js
            lat= js['result']['location']['lat']
            lng= js['result']['location']['lng']
            db.total_lianjia_copy.update({'name':addr,'city_name':city},{'$set':{'latidue':lat,'longtitude':lng}})
        except Exception,e:
            print "can't locate place ",city,addr
            continue
        time.sleep(random.random())
getcordinate()