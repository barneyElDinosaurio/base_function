# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class HeaderchangePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.doc = self.client['proxyip']['pool']
    def process_item(self, item, spider):
        self.doc.insert(dict(item))
        return item
