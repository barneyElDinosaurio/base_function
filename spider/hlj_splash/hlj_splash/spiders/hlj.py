# -*- coding: utf-8 -*-
import requests
import scrapy
import time
from scrapy import Request
from scrapy_splash import SplashRequest
from hlj_splash import config

'''
splash使用代理的例子
'''
class HljSpider(scrapy.Spider):
    name = 'hlj'
    test_url = 'http://httpbin.org/ip'

    def start_requests(self):
        # my_proxy = self.get_proxy()

        yield Request(
            url=self.test_url,
            meta={'splash':
                      {'args': {
                          'proxy': my_proxy,
                                'wait': 5},
                       'endpoint': 'render.html',
                       }
                  }
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
