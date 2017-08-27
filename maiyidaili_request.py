# coding: utf-8
import hashlib
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
testUrl='http://members.3322.org/dyndns/getip'
# 计算签名
timesp = '{}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
codes = app_secret + 'app_key' + my_app_key + 'timestamp' + timesp + app_secret
sign = hashlib.md5(codes.encode('utf-8')).hexdigest().upper()

# 拼接一个用来获得蚂蚁代理服务器的「准入」的 header (Python 的 concatenate '+' 比 join 效率高)
authHeader = 'MYH-AUTH-MD5 sign=' + sign + '&app_key=' + my_app_key + '&timestamp=' + timesp

# 用 Python 的 Requests 模块。先订立 Session()，再更新 headers 和 proxies
s = requests.Session()
s.headers.update({'Proxy-Authorization': authHeader})
s.proxies.update(mayi_proxy)
pg = s.get(testUrl)  # tuple: 300 代表 connect timeout, 270 代表 read timeout
#pg.encoding = 'GB18030'
print pg.text
print pg.status_code