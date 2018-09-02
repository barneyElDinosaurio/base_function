# -*- coding: utf-8 -*-
import scrapy
from headerchange.user_agents import agents
import random
import json

class HeadervalidationSpider(scrapy.Spider):
    name = 'headervalidation'

    def start_requests(self):
        url='http://httpbin.org/ip'
        for i in range(5):
            yield scrapy.Request(url=url,dont_filter=True)

    def parse(self, response):
        print('*'*20)
        print(response.text)
        # print(json.loads(response.body_as_unicode()).get('headers').get('User-Agent'))
        print('*'*20)
