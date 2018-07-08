from lxml import etree
import re
with open('temp.html','r') as f:
	tree = etree.HTML(f.read())

album=tree.xpath('//div[@class="albumTab-wrap"]')[0]
links =  album.xpath('.//p[@class="site-piclist_info_title"]/a/@href')
# print(len(links))
f=open('links.txt','a')
for i in links:
	# print(i)
	if re.match('http',i):
		print(i)
		f.write(i)
		f.write('\n')
f.close()