class UrlManager(object):

	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()


	def add_new_url(self,url):
		if url is not None and url not in self.old_urls and url not in self.new_urls:
			self.new_urls.add(url)


	def has_new_url(self):
		return self.new_urls_size()!=0


	def new_urls_size(self):
		return len(self.new_urls)


	def get_new_url(self):
		url = self.new_urls.pop()
		self.old_urls.add(url)
		return url

	def old_urls_size(self):
		return len(self.old_urls)

	def add_new_urls(self,urls):
		for url in urls:
			self.add_new_url(url)



import requests
class HtmlDownload(object):

	def download(self,url,retry=5):
		headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0'}
		for _ in range(retry):
			try:
				r = requests.get(url,headers=headers)
				if r.status_code==200:
					r.encoding='utf8'
					return r.text
				else:
					continue
			except Exception as e:
				print(e)

		return None


# from bs4 import BeautifulSoup
from lxml import etree
import urlparse
class HtmlParse(object):

	def parse(self,url,html):
		if url is None or html is None:
			return

		# soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
		tree = etree.HTML(html)
		data=self.get_data(url,tree)
		host='https://baike.baidu.com'
		urls =self.get_url(host,tree)
		# print('data: ',data)
		# print('url: ',urls)
		return data,urls

	def get_data(self,url,tree):
		data={}
		data['url']=url
		try:
			title = tree.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()')[0]
		except Exception as e:
			return None

		data['title']=title
		print(title)
		summary = tree.xpath('//div[@class="lemma-summary"]')
		s =''
		for i in summary:
			content= i.xpath('string(.)')
			print('content',content)
			s=s+content+' '

		data['summary']=s

		return data

	def get_url(self,host,tree):
		new_urls = set()
		for i in tree.xpath('//a[@target="_blank"]/@href'):
			url = urlparse.urljoin(host,i)
			new_urls.add(url)
		return new_urls



class SpiderCls(object):
	def __init__(self):
		self.manager = UrlManager()
		self.download=HtmlDownload()
		self.parser=HtmlParse()

	def crawl(self,root_url):
		self.manager.add_new_url(root_url)
		while (self.manager.has_new_url() and self.manager.old_urls_size() < 50 ):
			new_url =self.manager.get_new_url()
			html = self.download.download(new_url)
			data,urls = self.parser.parse(new_url,html)
			# print(data)
			# print(urls)

			self.manager.add_new_urls(urls)

obj =SpiderCls()

url = 'https://baike.baidu.com/item/M2/121'
obj.crawl(url)
