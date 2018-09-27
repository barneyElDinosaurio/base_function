# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request, FormRequest
import logging
import redis
from sandbox.items import SpiderItem
import pymongo
class WebsiteSpider(scrapy.Spider):

    name = 'website'
    headers = {
    }
    post_url = ''

    db = pymongo.MongoClient('10.18.6.102',port=27018)
    doc=db['spider']['carbin_hist']

    def start_requests(self):

        # TO DO
        URL = 'https://cha.zfzj.cn/'
        yield Request(url=URL, callback=self.query)

    def query(self, response):
        # TO DO
        rds = redis.StrictRedis('10.18.4.211',db=10,decode_responses=True)

        data = {
        }

        while 1:
            card=rds.lpop('continue_cardbin')
            if not card:
                break
            logging.info('query card >>>> {}'.format(card))
            data['inputValue']=card
            yield FormRequest(url=self.post_url,formdata=data,headers=self.headers,callback=self.parse,meta={'card':card,'page':1})


    def parse(self, response):

        ret_data = json.loads(response.body_as_unicode())
        card = response.meta['card']
        rows = ret_data['rows']
        self.doc.insert({'cardno':card})

        if not rows:
            return

        for row in rows:
            accountLength = row['accountLength']
            cardName = row['cardName']
            cardType = row['cardType']
            mainAccount = row['mainAccount']
            mainValue = row['mainValue']
            orgName = row['orgName']

            spiderItem= SpiderItem()

            for field in spiderItem.fields:
                try:
                    spiderItem[field]=eval(field)
                except Exception as e:
                    logging.warning('can not find define of {}'.format(field))
                    logging.warning(e)

            yield spiderItem






