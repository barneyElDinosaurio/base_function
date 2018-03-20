#-*-coding=utf-8-*-
import requests
class Download():

	def __init__(self):


	def download(self,url,retry):

		try:
			r=requests.get(url)
		except:

			return self.download(url,retry-1)
