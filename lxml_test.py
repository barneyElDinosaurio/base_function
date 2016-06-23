#-*-coding=utf-8-*-
__author__ = 'rocchen'
from lxml import html
from lxml import etree
import urllib2
def lxml_test():
    url="http://www.caixunzz.com"
    req=urllib2.Request(url=url)
    resp=urllib2.urlopen(req)
    #print resp.read()
    '''
    parse_body=html.fromstring(resp.read())
    href=parse_body.xpath('//a[@class="label"]/@href')
    print href
    #not working from above
    '''

    tree=etree.HTML(resp.read())
    href=tree.xpath('//a[@class="label"]/@href')
    #print href.tag
    for i in href:
        #print html.tostring(i)
        #print type(i)
        print i

    print type(href)
#not working yet

lxml_test()
