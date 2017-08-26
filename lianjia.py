# coding: utf-8
from lxml import etree
fp=open('lianjia_city.txt').read()
tree=etree.HTML(fp)
for i in tree.xpath('//li/a/@href'):
    print '\'https://m.lianjia.com'+i+'xiaoqu\','