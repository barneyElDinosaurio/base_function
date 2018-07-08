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
			try:
				result=self.cache[url]
			except KeyError:
				pass
		# else:
		# 	if

		if result is None:

			result = self.download(url)
			if self.cache:
				self.cache[url]=result

		return result['html']

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
		ret =  self.db.webpage.find_one({'_id':url})
		if ret:
			return ret['html']
		else:
			raise KeyError(url+'does not exist')

	def __setitem__(self, url, html):
		record={'html':html,'timestamp':datetime.datetime.utcnow()}
		self.db.webpage.update({'_id':url},{'$set':record},upsert=True)

def main():

	mongo=MongoCache()
	d=Download(cache=mongo)
	print(d('http://30daydo.com'))

if __name__== '__main__':
	main()