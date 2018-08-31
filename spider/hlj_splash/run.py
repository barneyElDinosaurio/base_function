# -*-coding=utf-8-*-
# @Time : 2018/8/10 14:30
# @File : run.py
from scrapy import cmdline
cmd ='scrapy crawl proxy_case'
# cmd ='scrapy crawl hlj'
cmdline.execute(cmd.split())
