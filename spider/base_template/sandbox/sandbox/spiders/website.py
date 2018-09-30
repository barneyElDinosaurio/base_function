# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request, FormRequest
import logging
import redis
from sandbox.items import SpiderItem


# get
class WebGetSpider(scrapy.Spider):
    name = 'website1'
    headers = {
        "Host": "cha.zfzj.cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://cha.zfzj.cn/mainPage.html",
    }
    URL = 'https://cha.zfzj.cn/bankCardDetail/select'

    def start_requests(self):
        # TO DO
        yield Request(url=self.URL)

    def parse(self, response):
        # logging.info(response.text)
        # logging.info('pass')
        ret_data = json.loads(response.body_as_unicode())


        spiderItem= SpiderItem()

        for field in spiderItem.fields:
            try:
                spiderItem[field]=eval(field)
            except Exception as e:
                logging.warning('can not find define of {}'.format(field))
                logging.warning(e)

        yield spiderItem

# post
class WebPostSpider(scrapy.Spider):
    name = 'website2'
    headers = {
        "Host": "cha.zfzj.cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko)",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://cha.zfzj.cn/mainPage.html",
    }
    post_url = 'https://cha.zfzj.cn/bankCardDetail/select'

    def start_requests(self):
        # TO DO
        URL = 'https://cha.zfzj.cn/'
        yield Request(url=URL, callback=self.query)

    def query(self, response):
        # TO DO
        rds = redis.StrictRedis('10.18.6.102',db=7,decode_responses=True)


        data = {
            "limit": "500",
            "offset": '1',
            "sortOrder": "asc",
            "inputValue": '',
        }

        while 1:
            card=rds.lpop('cardbin0925')
            if not card:
                break
            logging.info('query card >>>> {}'.format(card))
            data['inputValue']=card
            yield FormRequest(url=self.post_url,formdata=data,headers=self.headers,callback=self.parse,meta={'card':card,'page':1})


    def parse(self, response):
        # logging.info(response.text)
        # logging.info('pass')
        ret_data = json.loads(response.body_as_unicode())
        card = response.meta['card']
        rows = ret_data['rows']


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

        total = ret_data['total']
        pages = int(total / 500) if total % 500 == 0 else int(total / 500) + 1
        current_page = response.meta['page']
        if pages > current_page:
            current_page+=1
            data = {
                "limit": "500",
                "offset": str(current_page),
                "sortOrder": "asc",
                "inputValue": card,
            }
            yield FormRequest(url=self.post_url,headers=self.headers,formdata=data,meta={'page':current_page,'card':card})



