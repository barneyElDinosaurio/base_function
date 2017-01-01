#-*-coding=utf-8-*-

__author__ = 'Rocky'

import requests,datetime

'''
#url='http://www.zhihu.com'
url='http://httpbin.org/get'

header={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/66666 Firefox/33.0'}
s=requests.get(url,headers=header)
print s.text
print s.headers
zhihu_url="http://xueqiu.com"
#header={'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'}
z=requests.get(zhihu_url,headers=header)
print z.headers
print z.cookies


r = requests.get('http://github.com/timeline.json')
print r
'''

def requests_practise():
    url1='http://httpbin.org/get'
    agent='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    header={'User-Agent':agent}
    content=requests.get(url1)
    print content.text

start=datetime.datetime.now()
requests_practise()
end=datetime.datetime.now()
used=end-start
print used

def renren_access():
    url="http://www.renren.com/ajaxLogin/login"
    s=requests.Session()
    user={'email':'','password':''}
    r=