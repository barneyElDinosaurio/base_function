# coding: utf-8
import hashlib
import time
# import urllib2

# 请替换appkey和secret
import requests
def mayiproxy(url=None,headers={}):
    appkey = "104595392"
    secret = "c978952ede1661bd5342b34ca0bf561e"
    paramMap = {
        "app_key": appkey,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")  # 如果你的程序在国外，请进行时区处理
    }
    # 排序
    keys = paramMap.keys()
    keys.sort()
    # new_key = sorted(list(keys))

    codes = "%s%s%s" % (secret, str().join('%s%s' % (key, paramMap[key]) for key in keys), secret)
<<<<<<< HEAD
=======
    print('codes {}'.format(codes))
>>>>>>> origin/master
    print(codes)
    # 计算签名
    sign = hashlib.md5(codes).hexdigest().upper()
    print(sign)
    paramMap["sign"] = sign

    # 拼装请求头Proxy-Authorization的值
    keys = paramMap.keys()
    authHeader = "MYH-AUTH-MD5 " + str('&').join('%s=%s' % (key, paramMap[key]) for key in keys)
    proxy='http://s5.proxy.mayidaili.com:8123'
    # 接下来使用蚂蚁动态代理进行访问
    target='http://members.3322.org/dyndns/getip'
    headers['Proxy-Authorization'] = authHeader
    r=requests.get(url=target,headers=headers,proxies={'http':proxy})
    return r

print(mayiproxy())