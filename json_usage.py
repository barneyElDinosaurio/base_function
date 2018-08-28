# -*-coding=utf-8-*-
# @Time : 2018/8/20 13:38
# @File : json_usage.py

import ijson
import codecs
def json_usage():
    file = r'E:\store_data\meituan.json'
    start = 0
    with codecs.open(file,'r',encoding='utf8') as f:
        objects = ijson.parse(f)
        for prefix,event,value in objects:
            print(prefix,event,value)
            if start >200:
                break
            start+=1


def ijson_usage():
    with open('test.json','r') as f:
        objects = ijson.items(f,'earth.america.item')
        for o in objects:
            print(o)


ijson_usage()

