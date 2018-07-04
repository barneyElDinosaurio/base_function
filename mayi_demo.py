# -*-coding=utf-8-*-

def py3_case():
    import hashlib
    import time
    import requests

    # 找群主购买 my_app_key, myappsecret, 以及蚂蚁代理服务器的 mayi_url 地址和 mayi_port 端口
    my_app_key = "104595392"
    app_secret = "c978952ede1661bd5342b34ca0bf561e"
    mayi_url = 'http://s5.proxy.mayidaili.com'
    mayi_port = '8123'

    # 蚂蚁代理服务器地址
    mayi_proxy = {'http': 'http://{}:{}'.format(mayi_url, mayi_port)}

    # 准备去爬的 URL 链接
    url = 'http://members.3322.org/dyndns/getip'

    # 计算签名
    timesp = '{}'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
    codes = app_secret + 'app_key' + my_app_key + 'timestamp' + timesp + app_secret
    sign = hashlib.md5(codes.encode('utf-8')).hexdigest().upper()

    # 拼接一个用来获得蚂蚁代理服务器的「准入」的 header (Python 的 concatenate '+' 比 join 效率高)
    authHeader = 'MYH-AUTH-MD5 sign=' + sign + '&app_key=' + my_app_key + '×tamp=' + timesp

    # 用 Python 的 Requests 模块。先订立 Session()，再更新 headers 和 proxies
    s = requests.Session()
    s.headers.update({'Proxy-Authorization': authHeader})
    s.proxies.update(mayi_proxy)
    pg = s.get(url, timeout=(300, 270))  # tuple: 300 代表 connect timeout, 270 代表 read timeout
    # pg.encoding = 'GB18030'
    print(pg.text)



def py2_case():
    import hashlib
    import time
    import urllib2

    # 请替换appkey和secret
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

    print authHeader

    # 接下来使用蚂蚁动态代理进行访问

    proxy_handler = urllib2.ProxyHandler({"http": 'http://s5.proxy.mayidaili.com:8123'})
    opener = urllib2.build_opener(proxy_handler)

    request = urllib2.Request('http://members.3322.org/dyndns/getip')

    # // 将authHeader放入请求头中即可, 注意authHeader必须在每次请求时都重新计算，要不然会因为时间误差而认证失败
    request.add_header('Proxy-Authorization', authHeader)

    response = opener.open(request)

    print response.read()

py2_case()