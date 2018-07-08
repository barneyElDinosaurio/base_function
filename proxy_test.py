#-*-coding=utf-8-*-
# -*-*-

# -*-*-

# ! -*- encoding:utf-8 -*-
import re

import requests

#targetUrl = "https://beijing.anjuke.com/"
import time

targetUrl = "http://proxy.abuyun.com/switch-ip"
# targetUrl = "http://proxy.abuyun.com/current-ip"

proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

proxyUser = "HHE550O95000PASP"
proxyPass = "E3678EAC6820988E"
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
headers={'User-Agent':user_agent}
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}
while 1:
    #print(proxies)
    resp = requests.get(targetUrl, headers=headers)
    #resp = requests.get(targetUrl, headers=headers,proxies=proxies)
    time.sleep(2)

    print(resp.status_code)
    #print(resp.text)
    content = resp.text
    print(content)
    p = re.compile(u'请输入图片中的验证码')
    if p.findall(content):
        print("需要手动输入验证码")
        # return 404
        raw_input("打开浏览器，输入验证码后按Enter确认键继续")