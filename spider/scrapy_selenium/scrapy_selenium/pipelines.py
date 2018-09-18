# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ScrapySeleniumPipeline(object):
    def __init__(self):
        self.mongo = pymongo.MongoClient('127.0.0.1')
        self.doc = self.mongo['spider']['jd_book2']
    def process_item(self, item, spider):
        self.doc.insert(dict(item))
        return item
