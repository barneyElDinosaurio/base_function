# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GdcicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    enterprise = scrapy.Field()
    enterprise_link = scrapy.Field()
    punish_file = scrapy.Field()
    punish_file_no = scrapy.Field()
    punish_dept = scrapy.Field()
    punish_date = scrapy.Field()
    crawl_date = scrapy.Field()
