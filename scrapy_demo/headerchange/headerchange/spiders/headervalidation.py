# -*- coding: utf-8 -*-
import scrapy


class HeadervalidationSpider(scrapy.Spider):
    name = 'headervalidation'
    allowed_domains = ['helloacm.com']
    start_urls = ['http://helloacm.com/api/user-agent/']


    # def start_requests(self):
    #     header={'User-Agent':'Hello World'}
    #     yield scrapy.Request(url='http://helloacm.com/api/user-agent/',headers=header)

    def parse(self, response):
        print '*'*20
        print response.body
        print '*'*20
