# -*-coding=utf-8-*-
import hashlib

import time

import requests
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware


class CustomerUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = 'Personal Headers'
        request.headers.setdefault('User-Agent', ua)


class CustomProxy(object):
    def process_request(self, request, spider):
        # request.meta['']
        # time.sleep(1)
        # auth_header = self.get_auth_header()
        proxy = self.get_proxy()
        request.meta['proxy'] = proxy
        # request.headers['Proxy-Authorization'] = auth_header

    def get_proxy(self,retry=5):
        proxyurl = 'http://:8081/dynamicIp/common/getDynamicIp.do'
        count = 0
        for i in range(retry):
            try:
                r = requests.get(proxyurl, timeout=10)
            except Exception as e:
                print(e)
                count += 1
                print('代理获取失败,重试' + str(count))
                time.sleep(1)

            else:
                js = r.json()
                proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
                proxies_random = {
                    'http': proxyServer
                }
                return proxyServer

    '''
    def get_auth_header(self):
        # 请替换app_key和secret
        app_key = "xxxxxxxxx"
        secret = "xxxxxxxxxxxxx"

        param_map = {
            "app_key": app_key,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),  # 如果你的程序在国外，请进行时区处理
            "enable-simulate": 'true',
            "random-useragent": 'pc',
            "clear-cookies": 'true'
        }
        # 排序
        keys = param_map.keys()
        keys.sort()

        codes = "%s%s%s" % (secret, str().join('%s%s' % (key, param_map[key]) for key in keys), secret)

        # 计算签名
        sign = hashlib.md5(codes).hexdigest().upper()

        param_map["sign"] = sign

        # 拼装请求头Proxy-Authorization的值
        keys = param_map.keys()
        auth_header = "MYH-AUTH-MD5 " + str('&').join('%s=%s' % (key, param_map[key]) for key in keys)

        # print time.strftime("%Y-%m-%d %H:%M:%S")
        # print authHeader

        return auth_header
    '''
