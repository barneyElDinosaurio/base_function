#-*-coding=utf-8-*-
import requests
import pymongo
import datetime
class Download():

	def __init__(self,cache=None):
		self.headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0'}
		self.cache=cache


	def __call__(self, url):
		result=None
		if self.cache:
			result=self.cache[url]

		result = self.download(url)
		return result

	def download(self,url,retry=3):
		for _ in range(retry):
			try:
				r=requests.get(url,headers=self.headers)
				if r:
					return {'html':r.content,'code':r.status_code}
			except:
				continue
		return {'html':None,'code':500}


class MongoCache():

	def __init__(self,expires=datetime.timedelta(days=1)):
		self.client=pymongo.MongoClient('localhost',27017)
		self.db=self.client.cache
		self.db.webpage.create_index('timestamp',expireAfterSeconds=expires.total_seconds())
	def __getitem__(self, url):
		ret =  self.db.webpage.findone({'_id':url})
		if ret:
			return ret['html']
		else:
			raise KeyError(url+'does not exist')

	def __setitem__(self, key, value):
		self.db.webpage.insert({'_id':key,'html':value})

def main():
	d=Download()
	print d('http://30daydo.com')['html']

if __name__== '__main__':
	main()