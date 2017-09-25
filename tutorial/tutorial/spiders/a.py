# -*- coding: utf-8 -*-
import scrapy


class ASpider(scrapy.Spider):
    name = 'a'
    allowed_domains = ['http://30daydo.com']
    start_urls = ['http://http://30daydo.com/']

    def parse(self, response):
        pass
