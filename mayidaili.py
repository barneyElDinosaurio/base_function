# coding: utf-8
import hashlib
import time
import urllib2

# 请替换appkey和secret
appkey = "235817354"
secret = "9dab67c52899767b69d31b0c8ef06ebd"

paramMap = {
    "app_key": appkey,
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")  # 如果你的程序在国外，请进行时区处理
}
# 排序
keys = paramMap.keys()
keys.sort()

codes = "%s%s%s" % (secret, str().join('%s%s' % (key, paramMap[key]) for key in keys), secret)
print codes
# 计算签名
sign = hashlib.md5(codes).hexdigest().upper()
print sign
paramMap["sign"] = sign

# 拼装请求头Proxy-Authorization的值
keys = paramMap.keys()
authHeader = "MYH-AUTH-MD5 " + str('&').join('%s=%s' % (key, paramMap[key]) for key in keys)

print authHeader

# 接下来使用蚂蚁动态代理进行访问
test_url='https://lianyungang.anjuke.com/'
proxy_handler = urllib2.ProxyHandler({"http": 's3.proxy.mayidaili.com:8123'})
opener = urllib2.build_opener(proxy_handler)
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"

headers = {"User-agent": user_agent, 'upgrade-insecure-requests': '1',
                'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, br'}
request = urllib2.Request(url=test_url,headers=headers)

# 将authHeader放入请求头中即可, 注意authHeader必须在每次请求时都重新计算，要不然会因为时间误差而认证失败
request.add_header('Proxy-Authorization', authHeader)

response = opener.open(request)

print response.read()
