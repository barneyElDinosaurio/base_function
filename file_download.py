__author__ = 'rocky'
import urllib,urllib2,StringIO,gzip
url="http://image.xitek.com/photo/201001/13906/1390602/1390602_1262521000.jpg"
filname=url.split("/")[-1]
req=urllib2.Request(url)
resp=urllib2.urlopen(req)
content=resp.read()
#data = StringIO.StringIO(content)
#gzipper = gzip.GzipFile(fileobj=data)
#html = gzipper.read()
'''
f=open(filname,'w')
f.write()
f.close()
'''
#图片下载需要用到wb
with open(filname,'wb') as code:
    code.write(content)