# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
# from scrapy.http.
class LoginSpider(scrapy.Spider):
    name = 'login'
    # allowed_domains = ['scraping.com']
    # start_urls = ['http://scraping.com/']

    def start_requests(self):
    	login_url = 'http://example.webscraping.com/places/default/user/login?_next=/places/default/index'
    	yield Request(login_url,callback=self.login_web)

    def parse(self, response):
    	url = 'http://example.webscraping.com/places/default/user/profile?_next=/places/default/index'
        yield Request(url=url,callback=self.parse_item)

    def login_web(self,response):
    	fd={'email':'yagamil@126.com','password':'12345678'}
    	yield FormRequest.from_response(response,formdata=fd,callback=self.parse)

    def parse_item(self,response):
    	keys = response.css('table label::text').re('(.+):')
    	values = response.css('table td.w2p_fw::text').extract()
    	item= dict(zip(keys,values))
    	print('item:',item)
    	yield item