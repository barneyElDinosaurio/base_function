# -*-coding=utf-8-*-
from scrapy import cmdline
cmd = 'scrapy crawl quote -o result.csv'
cmdline.execute(cmd.split())