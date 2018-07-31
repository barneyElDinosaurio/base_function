# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
import urllib
import hashlib

# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
import requests
def addr_poi():
    city='哈尔滨'
    addr='星河湾'
    ak_code=''
    queryStr = '/geocoder/v2/?city=%s&address=%s&ret_coordtype=bd09ll&output=json&ak=%s' %(city,addr,ak_code)
    #queryStr = '/geocoder/v2/?address=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO' %addr
    #queryStr='/place/v2/search?q=银河小区&region=杭州市&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO'

    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

    # 在最后直接追加上yoursk
    rawStr = encodedStr + ''

    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
    sn= hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
    #print(sn)
    #url='http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&sn=%s' %(addr,sn)
    url='http://api.map.baidu.com/geocoder/v2/?city=%s&address=%s&ret_coordtype=bd09ll&output=json&ak=%s&sn=%s' %(city,addr,ak_code,sn)
    #url='http://api.map.baidu.com/place/v2/search?q=银河小区&region=杭州市&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&sn=%s' %sn
    s=requests.get(url)
    print(s.text)
    js=s.json()
    try:
        lng = js['result']['location']['lng']
        lat = js['result']['location']['lat']
    except Exception as e:
        print(e)
        lng = '0'
        lat = '0'

    return lat, lng

def poi_addr():
    #city = '深圳市'
    #addr = '滨苑住宅小区8栋'
    lat='22.535473'
    lng='114.07278'
    ak_code=''
    # http://api.map.baidu.com/geocoder/v2/?callback=renderReverse&location=39.983424,116.322987&output=json&pois=1&ak=您的ak
    queryStr = '/geocoder/v2/?location=%s,%s&output=json&pois=0&coordtype=bd09mc&ak=%s' % (lat,lng ,ak_code)
    # queryStr = '/geocoder/v2/?address=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO' %addr
    # queryStr='/place/v2/search?q=银河小区&region=杭州市&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO'

    # 对queryStr进行转码，safe内的保留字符不转换
    encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

    # 在最后直接追加上yoursk
    rawStr = encodedStr + 'HWMYuBMbfW6sooCmN487953tY495T9vn'

    # md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
    # 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
    sn = hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
    # print(sn)
    # url='http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&sn=%s' %(addr,sn)
    url = 'http://api.map.baidu.com/geocoder/v2/?location=%s,%s&output=json&pois=0&coordtype=bd09mc&ak=%s&sn=%s' % (lat, lng, ak_code,sn)
    # url='http://api.map.baidu.com/place/v2/search?q=银河小区&region=杭州市&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&sn=%s' %sn
    s = requests.get(url)
    print(s.text)
    js = s.json()
    print(js)
    print(js['result']['location'])
    # print(js['msg'])
    try:
        for k, v in js['result'].items():
            print(k, v)
    except Exception, e:
        print(e)

poi_addr()
#x,y=addr_poi()
#print(x,y)