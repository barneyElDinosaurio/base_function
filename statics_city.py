# coding: utf-8
import codecs
import json

import pymongo

client=pymongo.MongoClient('127.0.0.1',27017)

db=client.anjuke_mobile
collection=db.mobile_complete
fp=codecs.open('new_city.txt','r',encoding='utf-8')
content=fp.read()
js=json.loads(content)
#print js
for k,v in js.items():
    #print v
    num=collection.find({'city_name':v})
    l=list(num)
    if len(l)!=0:
        print v, "\t", len(list(l))

