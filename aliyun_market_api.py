# import urllib, 
import sys,json
import ssl
import urllib.request
from urllib import parse
'''
阿里云市场的一些api
'''

host = 'https://jisuznwd.market.alicloudapi.com'
path = '/iqa/query'
method = 'GET'
appcode = 'e44b5b8f74ce47ebb3a202dfab10002c'
q='习近平最近怎么啦'

encode_q=parse.quote(q)
print(encode_q)
querys = 'question={}'.format(encode_q)

bodys = {}
url = host + path + '?' + querys

req = urllib.request.Request(url)
req.add_header('Authorization', 'APPCODE ' + appcode)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
response = urllib.request.urlopen(req, context=ctx)
content = response.read()
# print(content)
str_content =str(content,'utf-8')
if (content):
    # print(content)
    js=json.loads(str_content)
    print(js['result']['content'])