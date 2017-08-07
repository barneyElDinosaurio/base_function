# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
#from scrapy import Spider
import scrapy
from scrapy.selector import HtmlXPathSelector
number=0
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains=['toscrape.com']
    #start_urls=

    def start_requests(self):
        url=['http://quotes.toscrape.com/page/1/',
             'http://quotes.toscrape.com/page/2/']

        for i in url:

            #yield scrapy.Request(url=i,callback=self.parse)
            yield self.make_requests_from_url(i)

    def parse(self, response):
        #print response.url.split('/')
        #sel=HtmlXPathSelector(response)

        content=response.xpath('//div[@class="quote"]')
        for x in  content:
            word= x.xpath('.//span[@class="text"]/text()').extract_first()
            print '\n'
            print word
            yield {'text':word}

        nextPage=response.css('li.next a::attr(href)').extract_first()
        if  nextPage is not None:
            goNext=response.urljoin(nextPage)
            print "Go next: ",goNext
            yield scrapy.Request(url=goNext,callback=self.parse)