# -*-coding=utf-8-*-
__author__ = 'rocchen'
from lxml import html
from lxml import etree
import urllib2, requests


def lxml_test():
    url = "http://www.caixunzz.com"
    req = urllib2.Request(url=url)
    resp = urllib2.urlopen(req)
    #print(resp.read())
    '''
    parse_body=html.fromstring(resp.read())
    href=parse_body.xpath('//a[@class="label"]/@href')
    print(href)
    #not working from above
    '''

    tree = etree.HTML(resp.read())
    href = tree.xpath('//a[@class="label"]/@href')
    #print(href.tag)
    for i in href:
        #print(html.tostring(i))
        #print(type(i))
        print(i)

    print(type(href))

#not working yet
session = requests.session()
import cookielib

session.cookies = cookielib.LWPCookieJar(filename="cookies")
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {'Host': 'www.zhihu.com',
           'Referer': 'https://www.zhihu.com',
           'User-Agent': agent}


def lxml_text():
    url = 'https://www.zhihu.com/question/20401952/answer/21764432'
    s = requests.get(url, headers=headers).text
    #print(s)
    tree = etree.HTML(s)
    content = tree.xpath('//div[@class="zm-editable-content clearfix"]')
    print(content)
    for i in content:
        print(i.xpath('string(.)'))



def lxml_case():
    r=requests.get('http://30daydo.com')
    t=etree.HTML(r.text)
    s=t.xpath('//div[@class="aw-item article"]')
    print(s)
#lxml_text()

#lxml_case()

def lxml_case2():
    #网站的例子
    str1='''
    <bookstore>

    <book>
      <title>Harry Potter</title>
      <author>J K. Rowling</author>
      <year>2005</year>
      <price>29.99</price>
    </book>
    
    </bookstore>
    '''
    tree=etree.HTML(str1)
    t1=tree.xpath('bookstore')
    print(t1)

def lxml_case3():


    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item><span>Hello world</span></a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
             <li class="de-item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    '''

    tree=etree.HTML(text)
    html_s=etree.tostring(tree)
    print(html_s)
    #print(tree.xpath('//li//span/text()')[0])
    '''
    reg_case=tree.xpath('//*[starts-with(@class,"item")]')
    for i in reg_case:
        print(i.xpath('.//a/@href'))
    '''
    result=tree.xpath(r'//*[re:match(@class, "item-0")]')
    print(result)

    for i in result[0]:
        print(i.xpath('.//a/@href'))

lxml_case3()