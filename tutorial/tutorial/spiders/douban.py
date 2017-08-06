# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
from scrapy.spider import BaseSpider
from scrapy.http import Request
import os
class DoubanMovie(BaseSpider):

    name='douban'
    allowed_domains=['movie.douban.com']
    start_urls=[]
    def start_requests(self):
        print os.getcwd()
        movie_names=open('film_name.txt','r').readlines()
        #print movie_names

        base_url='http://movie.douban.com/subject_search?search_text='
        for i in movie_names:
            i=i.strip().replace(' ','+')
            print i
            self.start_urls.append(base_url+i)

        for i in self.start_urls:

            yield self.make_reuqests_from_url(i)


    def parse(self,response):
        print response.body