# -*- coding: utf-8 -*-
# @Time : 2018/8/26 18:52
# @File : run.py
from scrapy import cmdline

name = 'seluium_demo'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())
