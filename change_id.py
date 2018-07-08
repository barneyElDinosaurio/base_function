# coding: utf-8
from __future__ import unicode_literals
import json
import codecs
#null = None
#global null
'''
with codecs.open('houseinfo_11.json','r',encoding='utf-8') as fp:
    data=fp.readlines()
'''
#for x in data:
    #print(x)
with codecs.open('anjuke_m1.json','r') as fp:
    data=fp.readlines()
'''
for x in data:
    print(x)
'''

number_list=[number for number in xrange(1000000,2000000)]

op=codecs.open('anjuke_with_position2.json','w',encoding='utf-8')

new_dict={}
for index,line in enumerate(data):
    #print(line)
    linex=line
    #print(linex)
    #js=json.loads(linex,ensure_ascii=False)
    js=json.loads(linex)
    #temp_price=js['price']['2017-07'][0]['price']
    #print(temp_price)
    #print(js)
    #js=eval(line)
    #js['price']=temp_price

    js['_id']=number_list[index]
    '''
    for k,v in js.items():
        print(k,v)

        new_key=k
        new_value=v
        new_dict={new_key:new_value}
        #print(new_value)
    '''
    str1=json.dumps(js,ensure_ascii=False)

    #print(str1)
    op.write(str1)
    op.write('\n')

#op.close()

    #print(line)

