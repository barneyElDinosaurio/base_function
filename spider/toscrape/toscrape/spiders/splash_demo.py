# -*-coding=utf-8-*-
# @Time : 2018/8/16 11:24
# @File : splash_demo.py# -*- coding: utf-8 -*-
import requests
import scrapy
import time
from scrapy_splash import SplashRequest
from toscrape.items import ToscrapeItem

lua_script = '''
function main(splash)
    splash:go(splash.args.url)
    splash:wait(5)
    return splash:html()
end
'''

MYPROXY = '''splash:on_request(function(request)
    request:set_proxy{
        host = {0},
        port = {1},
    }
    return splash:html()
end)'''


class SplashSpider(scrapy.Spider):
    name = 'quote'
    # allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/js']

    def start_requests(self):
        for url in self.start_urls:
            # proxy = self.get_proxy()
            # port = proxy.split(':')[-1]
            # host = ':'.join(proxy.split(':')[:2])
            # print(host)
            # ret_proxy = MYPROXY.format(host, port)
            # yield SplashRequest(url=url, args={'images': 0, 'timeout': 10.1, 'wait': 9.1, 'proxy': proxy})
            yield SplashRequest(url=url, args={'images': 0, 'timeout': 10.1, 'wait': 9.1})
            # yield SplashRequest(url=url, args={'images': 0, 'timeout': 10,'lua_source':lua_script},endpoint='execute',cache_args=['lua_source'])

    def parse(self, response):
        for sel in response.xpath('//div[@class="quote"]'):
            item = ToscrapeItem()
            quote_ = sel.xpath('.//span[@class="text"]/text()').extract_first()
            author_ = sel.xpath('.//span/small/text()').extract_first()
            item['quote'] = quote_
            item['author'] = author_

            yield item
        url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if url:
            next_url = response.urljoin(url)
            # yield SplashRequest(url=next_url, args={'timeout': 10, 'images': 0,'lua_source':lua_script},endpoint='execute',cache_args=['lua_source'])
            # proxy = self.get_proxy()
            # proxy = self.get_proxy()
            # port = proxy.split(':')[-1]
            # host = ':'.join(proxy.split(':')[:2])
            # ret_proxy = MYPROXY.format(host, port)
            yield SplashRequest(url=next_url,
                                args={'timeout': 10.1, 'images': 0, 'wait': 9.1})

    def get_proxy(self, retry=50):
        proxyurl = 'http://:8081/dynamicIp/common/getDynamicIp.do'.format()
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
