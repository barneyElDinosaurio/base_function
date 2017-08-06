# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
#from scrapy import Spider
import scrapy
from scrapy.selector import HtmlXPathSelector
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains=['toscrape.com']
    #start_urls=

    def start_requests(self):
        url=['http://quotes.toscrape.com/page/1/',
             'http://quotes.toscrape.com/page/2/']

        for i in url:
            yield scrapy.Request(url=i,callback=self.parse)


    def parse(self, response):
        #print response.url.split('/')
        #sel=HtmlXPathSelector(response)

        content=response.xpath('//div[@class="quote"]')
        for x in  content:
            word= x.xpath('.//span[@class="text"]/text()').extract_first()
            print '\n'
            yield {'text':word}