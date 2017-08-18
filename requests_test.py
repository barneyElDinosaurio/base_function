# -*-coding=utf-8-*-

__author__ = 'Rocky'
from toolkit import Toolkit
import requests, datetime
import cookielib
from lxml import etree

session = requests.session()

session.cookies = cookielib.LWPCookieJar(filename="cookies")
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {'Host': 'xueqiu.com',
           'Referer': 'https://xueqiu.com/',
           'Origin': 'https://xueqiu.com',
           'User-Agent': agent}
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
    url1 = 'http://httpbin.org/get'
    agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    header = {'User-Agent': agent}
    content = requests.get(url1)
    print content.text
    print type(content.status_code)


start = datetime.datetime.now()
requests_practise()
end = datetime.datetime.now()
used = end - start
print used


def renren_access():
    url = "http://www.renren.com/ajaxLogin/login"
    s = requests.Session()
    user = {'email': '', 'password': ''}


def request_test():
    url = 'https://github.com/timeline.json'
    r = requests.get(url)
    print r.text
    print r.json()

    data = {"name": "Rocky"}
    url2 = "http://httpbin.org/post"
    s = requests.post(url2, data)
    print s.text
    print s.url
    t = requests.post(url2, params=data)
    print t.url


def request_test2():
    url = 'http://yuepaowanimal.tumblr.com/api/read?type=video&num=50&start=0'
    result = requests.get(url).text
    print result


def status_code_test():
    url = 'https://www.zhihu.com/collection/47548799?page=5'
    s = session.get(url, headers=headers, allow_redirects=False)
    print s.text
    print s.status_code


#request_test2()
def bbs_filename_check():
    url = 'http://bbs.sysu.edu.cn/bbstcon?board=Love&file=M.1104508652.A'
    headers = {'User-Agent': agent}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'gbk'
    content = resp.text
    tree = etree.HTML(content)
    title = tree.xpath('//title/text()')[0]
    print title
    filename = Toolkit.filename_filter(title)
    print filename

#status_code_test()
#bbs_filename_check()
requests_practise()