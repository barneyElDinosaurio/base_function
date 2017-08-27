# coding: utf-8
import hashlib
import re
import time
import requests

# 找群主购买 my_app_key, myappsecret, 以及蚂蚁代理服务器的 mayi_url 地址和 mayi_port 端口
my_app_key = "235817354"
app_secret = "9dab67c52899767b69d31b0c8ef06ebd"
mayi_url = 's3.proxy.mayidaili.com'
mayi_port = '8123'

# 蚂蚁代理服务器地址
mayi_proxy = {'http': 'http://{}:{}'.format(mayi_url, mayi_port)}

# 准备去爬的 URL 链接
#url = 'http://1212.ip138.com/ic.asp'
testUrl='https://km.anjuke.com'
# 计算签名
timesp = '{}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
codes = app_secret + 'app_key' + my_app_key + 'timestamp' + timesp + app_secret
sign = hashlib.md5(codes.encode('utf-8')).hexdigest().upper()

# 拼接一个用来获得蚂蚁代理服务器的「准入」的 header (Python 的 concatenate '+' 比 join 效率高)
authHeader = 'MYH-AUTH-MD5 sign=' + sign + '&app_key=' + my_app_key + '&timestamp=' + timesp

# 用 Python 的 Requests 模块。先订立 Session()，再更新 headers 和 proxies
s = requests.Session()
#s.headers.update({'Proxy-Authorization': authHeader})
s.proxies.update(mayi_proxy)

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"

headers = {"User-agent": user_agent, 'upgrade-insecure-requests': '1',
                'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br'}
s.headers.update(headers)
s.headers.update({'Proxy-Authorization': authHeader})
while 1:
    pg = s.get(testUrl)  # tuple: 300 代表 connect timeout, 270 代表 read timeout
    #pg.encoding = 'GB18030'
    #print pg.text
    p = re.compile(u'请输入图片中的验证码')
    if p.findall(pg.text):
        print "需要手动输入验证码"
        # return 404
        raw_input("打开浏览器，输入验证码后按Enter确认键继续")
    print pg.status_code
    time.sleep(5)