#-*-coding=utf-8-*-
'''
book <用python写网络爬虫>
'''
import requests
import urllib2
import re
import itertools
import urlparse
import redis
from collections import defaultdict
r = redis.Redis(host='127.0.0.1',port=6379,db=2)

'''
查看一个网站的robots协议。
'''
def check_robots(url):
	ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
	headers = {'User-Agent':ua}
	try:
		r = requests.get(url+'/robots.txt',headers=headers)
	except Exception as e:
		print(e)
		return None
	
	print(r.text)

def show_robots():
	url_list=['http://30daydo.com']
	[check_robots(i) for i in url_list]

'''
书中的基本代码
'''

def download(url,retry_num=3):
	ua = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
	headers = {'User-Agent':ua}
	req=urllib2.Request(url,headers=headers)
	try:
		html = urllib2.urlopen(req).read()

	except urllib2.URLError as e:
		print('Download error',e.reason)
		html=None
		if retry_num > 0:
			if hasattr(e,'code') and 500 < e.code < 600:
				return download(url,retry_num-1)

	return html


def crawl_sitemap(url):
	sitemap = download(url)
	print(sitemap)


def loop_test():
	for page in itertools.count(1):
		print(page)

def get_link(content,reg):
	re.findall(reg,content)

def link_crawler(seed_url,max_depth=2):
	crawl_queue=[seed_url]
	# seen=set(crawl_queue)
	seen={}
	seen[seed_url]=0
	while crawl_queue:
		url=crawl_queue.pop()
		print(url)
		html=download(url)
		links=re.findall('<a[^>]+href=["\'](.*?)["\']',html,re.IGNORECASE)
		# defaultdict()
		depth=seen[url]
		if seen[url]<max_depth:
			for link in links:
				# print(link)
				url_link=urlparse.urljoin(seed_url,link)
				# if seen[url]
				if url_link not in seen:
					# seen.add(url_link)
					seen[url_link]=depth+1
					r.lpush('url',url_link)
					crawl_queue.append(url_link)

def main():
	# url='http://www.douban.com/sitemap.xml'
	# show_robots()
	# print(download('http://zhihu.com'))
	# crawl_sitemap(url)
	# loop_test()
	url='http://example.webscraping.com/places/default/index/'
	link_crawler(url)

if __name__=='__main__':
	main()