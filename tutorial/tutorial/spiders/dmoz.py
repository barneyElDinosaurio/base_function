# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
from scrapy.spider import Spider
from scrapy.http import Request,FormRequest

class DmozSpider(Spider):
    name = '30daydo'
    allowed_domains=['30daydo.com']
    start_urls=["http://30daydo.com"
        ]

    #now this method has been ban by this website
    '''
    def parse(self, response):
        filename=response.url.spilt('/')[-2]
        open(filename,'wb').write(response.body)
    '''

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        self.header = {"User-Agent": self.user_agent}



    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url,headers=self.header,callback=self.parse_item)

    def parse_item(self,response):
        #filename=response.url.spilt('/')[-2]
        print response.body
        #open(filename,'wb').write(response.body)