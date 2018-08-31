# -*- coding: utf-8 -*-
import requests
import scrapy
import time
from scrapy_splash import SplashRequest
from hlj_splash import config
class ProxyCaseSpider(scrapy.Spider):
    name = 'proxy_case'
    test_url = 'http://httpbin.org/ip'

    def start_requests(self):
        proxy=self.get_proxy()
        print('proxy ip {}'.format(proxy))
        yield SplashRequest(
            url=self.test_url,
            args={'proxy':proxy},
            endpoint='render.html'
                            )

    def parse(self, response):
        print(response.text)

    def get_proxy(self, retry=5):
        proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
        for i in range(1, retry + 1):
            try:
                r = requests.get(proxyurl, timeout=10)
            except Exception as e:
                print(e)
                print('Failed to get proxy ip, retry ' + str(i))
                time.sleep(1)
            else:
                js = r.json()
                proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
                return proxyServer
        return None