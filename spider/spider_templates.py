# -*-coding=utf-8-*-
# @Time : 2018/7/30 10:31
# @File : spider_templates.py
import requests
url = 'http://was.zhuhai.gov.cn:8182/was5/web/search?channelid=290060&searchword=92440400MA4X7RC887'
r = requests.get(url)
r.encoding='utf-8'
print(r.text)
