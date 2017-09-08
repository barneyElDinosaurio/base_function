# coding: utf-8

# -*- coding: utf-8 -*-
# 第一行必须有，否则报中文字符非ascii码错误
import urllib
import hashlib

# 以get请求为例http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak
import requests

queryStr = '/geocoder/v2/?address=深圳市欧陆经典&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO'

# 对queryStr进行转码，safe内的保留字符不转换
encodedStr = urllib.quote(queryStr, safe="/:=&?#+!$,;'@()*[]")

# 在最后直接追加上yoursk
rawStr = encodedStr + 'HWMYuBMbfW6sooCmN487953tY495T9vn'

# md5计算出的sn值7de5a22212ffaa9e326444c75a58f9a0
# 最终合法请求url是http://api.map.baidu.com/geocoder/v2/?address=百度大厦&output=json&ak=yourak&sn=7de5a22212ffaa9e326444c75a58f9a0
sn= hashlib.md5(urllib.quote_plus(rawStr)).hexdigest()
print sn
url='http://api.map.baidu.com/geocoder/v2/?address=深圳市欧陆经典&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&sn=%s' %sn
s=requests.get(url)
js=s.json()
print js['result']
for k,v in js['result'].items():
    print k,v
'''
for k,v in s.json().items():
    print k,v
    #print v['result']
'''

url='http://api.map.baidu.com/geocoder/v2/?address=深圳市欧陆经典&output=json&ak=pmBkd1mBGETE07Bmp0WW4KlOHz7AZbiO&callback=showLocation'
s2=requests.get(url)
print s2.json()