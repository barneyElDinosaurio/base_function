# coding: utf-8
# -*-*-
# 感谢骚男 『zh (QQ: 315393472)』 提供的源代码
# -*-*-

# ! -*- encoding:utf-8 -*-
import re
import urllib2

# 要访问的目标页面
#targetUrl = "http://.anjuke.com/"
import time

targetUrl = "http://proxy.abuyun.com/switch-ip"
# targetUrl = "http://proxy.abuyun.com/current-ip"

# 代理服务器
proxyHost = "http-pro.abuyun.com"
proxyPort = "9010"

# 代理隧道验证信息
proxyUser = "HHE550O95000PASP"
proxyPass = "E3678EAC6820988E"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxy_handler = urllib2.ProxyHandler({
    "http": proxyMeta,
    "https": proxyMeta,
})
while 1:
    opener = urllib2.build_opener(proxy_handler)
    # opener.addheaders = [("Proxy-Switch-Ip", "yes")]
    urllib2.install_opener(opener)
    resp = urllib2.urlopen(targetUrl).read()
    '''
    p = re.compile(u'请输入图片中的验证码')
    if p.findall(resp):
        print "需要手动输入验证码"
        # return 404
        raw_input("打开浏览器，输入验证码后按Enter确认键继续")
    '''
    print resp
    time.sleep(2)

