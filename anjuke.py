# coding: utf-8
import json
import re
import urllib

import requests
def query(kw):
    for i in range(1,10):
        encode_kw=urllib.quote(kw)
        print i
        url='https://m.anjuke.com/ajax/autocomplete/?city_id=13&kw=%s&from=1&callback=jsonp%d' %(encode_kw,i)
        s=requests.Session()
        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
        js=s.get(url,headers=headers)
        print js.status_code
        #print js.text
        try:
            result=re.findall('jsonp7\((.*?)\);',js.text)[0]
            dic=json.loads(result)
            print '*'*20
            print dic['data']['match'][0]['comm_id']
        except Exception,e:
            print e
query('南方明珠花园二期1栋')