#-*-coding=utf-8-*-
__author__ = 'rocchen'
from lxml import html
import urllib2
def lxml_test():
    url="http://www.caixunzz.com"
    req=urllib2.Request(url=url)
    resp=urllib2.urlopen(req)
    #print resp.read()
    parse_body=html.fromstring(resp.read())
    href=parse_body.xpath('//a[@class="label"]/@href')
    print href
    for i in href:
        print html.tostring(i)
#not working yet

lxml_test()
