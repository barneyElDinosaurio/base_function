# -*- coding: utf-8 -*-
import scrapy


class ProxyautoSpider(scrapy.Spider):
    name = 'proxyauto'
    allowed_domains = ['3322.org']

    def start_requests(self):
        header={'User-Agent':"Mozilla\/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/62.0.3202.94 Safari\/537.36"}
        for _ in range(20):
            yield scrapy.Request(url='http://members.3322.org/dyndns/getip',headers=header,dont_filter=True)

    def parse(self, response):
        print '*'*20
        print response.body
        print '*'*20
