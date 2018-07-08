# coding: utf-8
import requests

headers={'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch', 'Host': '192.168.13.39:7789', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1', 'Connection': 'keep-alive', 'Cookie': 'sessionid=150076c22bd2d05992e270b5ded714fb', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

url = 'http://192.168.13.39:7789/crm/search_customer_company_api'
r = requests.get(url=url, headers=headers, params={'name': u'中国移动', 'limit': 10, 'offset': 10})
print(r.status_code)
print(r.text)
req_data = r.json()
print(req_data)

for i in req_data['rows']['customer_list']:
    for k, v in i.items():
        print(k, v)
'''
for i in r.json():
    print(i)
'''
