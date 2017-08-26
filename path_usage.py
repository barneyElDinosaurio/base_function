# coding: utf-8
import os
'''
print os.path.dirname(os.path.abspath(__file__))
temp= os.path.abspath(os.path.join(os.path.dirname(__file__),"../temp/HouseInfo"))
file= os.path.join(temp,'Qfang.py')
print file
with open(file,'r') as f:
    print f.read()

print os.path.dirname(os.path.abspath("__file__"))
print os.path.pardir
print os.path.join(os.path.dirname("__file__"),os.path.pardir)
print os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
'''
import os
def testcase1():
    files=os.listdir('.')
    for i in files:
        try:
            if 'xls'==i.split('.')[1]:
                print i
        except:
            continue

testcase1()


