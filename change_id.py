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
    #print x
<<<<<<< HEAD
with codecs.open('houseinfo_831.json','r') as fp:
=======
with codecs.open('houseinfo_all.json','r') as fp:
>>>>>>> origin/master
    data=fp.readlines()
'''
for x in data:
    print x
'''

number_list=[number for number in xrange(1000000,2000000)]

<<<<<<< HEAD
op=codecs.open('xiaoqu_LI_08_31.txt','w',encoding='utf-8')
=======
op=codecs.open('xiaoqu_all.txt','w',encoding='utf-8')
>>>>>>> origin/master
new_dict={}
for index,line in enumerate(data):
    #print line
    linex=line
    #print linex
    #js=json.loads(linex,ensure_ascii=False)
    js=json.loads(linex)

    #print js
    #js=eval(line)


    js['_id']=number_list[index]
    '''
    for k,v in js.items():
        print k,v

        new_key=k
        new_value=v
        new_dict={new_key:new_value}
        #print new_value
    '''
    str1=json.dumps(js,ensure_ascii=False)

    print str1
    op.write(str1)
    op.write('\n')

op.close()

    #print line

