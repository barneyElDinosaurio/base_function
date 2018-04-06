# -*-coding=utf-8-*-
# Get your range of csdn
__author__ = 'rocky'
import urllib2
import re
import time

link = 'http://blog.csdn.net/yagamil/article/details/52858314'
user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
header = {"User-Agent": user_agent}
req = urllib2.Request(link, headers=header)
retry=5
stop=False
for _ in range(retry):
    try:
        resp = urllib2.urlopen(req)
        stop=True
        break
    except Exception,e:
        print e
        continue
if not stop:
    exit(1)
content = resp.read()
# p = re.compile(r'<li>排名：<span>(.*?)</span></li>')
p = re.compile(r'    <div class="gradeAndbadge gradewidths" title="(\d+)">')
result = p.findall(content)
# print result[2]

today = time.strftime("%Y-%m-%d")
print today

f = open("csdn_range.txt", 'a')
contents = today + '\t' + result[0] + '\n'
f.write(contents)
f.close()
