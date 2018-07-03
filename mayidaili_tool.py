# coding: utf-8
import hashlib
import time
import urllib2

# 请替换appkey和secret
import requests
def useproxy(url,headers,postdata=None,post=False):
    appkey = "104595392"
    secret = "c978952ede1661bd5342b34ca0bf561e"
    paramMap = {
        "app_key": appkey,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")  # 如果你的程序在国外，请进行时区处理
    }
    # 排序
    keys = paramMap.keys()
    keys.sort()

    codes = "%s%s%s" % (secret, str().join('%s%s' % (key, paramMap[key]) for key in keys), secret)
    # 计算签名
    sign = hashlib.md5(codes).hexdigest().upper()
    paramMap["sign"] = sign

    # 拼装请求头Proxy-Authorization的值
    keys = paramMap.keys()
    authHeader = "MYH-AUTH-MD5 " + str('&').join('%s=%s' % (key, paramMap[key]) for key in keys)
    proxy='http://s5.proxy.mayidaili.com:8123'
    # 接下来使用蚂蚁动态代理进行访问
    #target='http://members.3322.org/dyndns/getip'
    headers['Proxy-Authorization'] = authHeader
    if post:
        try:
            r = requests.post(url=url, headers=headers, proxies={'http': proxy},data=postdata)
            #print 'in post'
            #print r.text
        except Exception as e:
            return None
    else:
        try:
            r=requests.get(url=url,headers=headers,proxies={'http':proxy})
        except Exception as e :
            return None
    return r
