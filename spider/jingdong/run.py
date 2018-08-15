# -*-coding=utf-8-*-
# @Time : 2018/8/15 16:01
# @File : run.py
from scrapy import cmdline
name = 'jd_book'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())