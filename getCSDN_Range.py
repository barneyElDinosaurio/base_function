#-*-coding=utf-8-*-
#Get your range of csdn
__author__ = 'rocky'
import urllib2,re
import time
link='http://blog.csdn.net/yagamil/article/details/52858314'
user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
header = {"User-Agent": user_agent}
req = urllib2.Request(link, headers=header)
resp = urllib2.urlopen(req)
content = resp.read()
#print content
p=re.compile(r'<li>排名：<span>第(\d+)名</span></li>')
result=p.findall(content)
print result[0]

today=time.strftime("%Y-%m-%d")
print today

f=open("csdn_range.txt",'a')
contents=today+'\t'+result[0]+'\n'
f.write(contents)
f.close()