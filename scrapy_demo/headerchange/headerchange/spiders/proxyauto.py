# -*- coding: utf-8 -*-
import scrapy
from headerchange.items import HeaderchangeItem

class ProxyautoSpider(scrapy.Spider):
    name = 'proxyauto'
    # allowed_domains = ['3322.org']

    def start_requests(self):
        header={'User-Agent':"Mozilla\/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/62.0.3202.94 Safari\/537.36"}
        for _ in range(200):
            yield scrapy.Request(url='http://members.3322.org/dyndns/getip',headers=header,dont_filter=True)

    def parse(self, response):
        item = HeaderchangeItem()
        # print('*'*20)
        # print(response.text)
        # print('*'*20)
        item['ip']=response.text
        yield item
