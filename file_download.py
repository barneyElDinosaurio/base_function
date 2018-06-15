__author__ = 'rocky'
import urllib, urllib2, StringIO, gzip, requests

def basic_download():
	url = "http://image.xitek.com/photo/201001/13906/1390602/1390602_1262521000.jpg"
	url2 = 'http://www.juchifs.com/Captcha.aspx'
	filname = url.split("/")[-1]
	req = urllib2.Request(url2)
	resp = urllib2.urlopen(req)
	content = resp.read()
	# data = StringIO.StringIO(content)
	#gzipper = gzip.GzipFile(fileobj=data)
	#html = gzipper.read()
	'''
	f=open(filname,'w')
	f.write()
	f.close()
	'''

	with open("code.gif", 'wb') as code:
	    code.write(content)

	requests.get(url2)


def process(block_number,block_size,totalsize):
	'''

	'''

	per = block_number * block_size * 100/totalsize
	if per > 100:
		per =100
	print('current process: {}'.format(per))

def download():
	url = 'http://down10.zol.com.cn/ceshi/ZZDS_4.7.0.0_zol.exe'
	urllib.urlretrieve(url,'localname.exe',process)

download()