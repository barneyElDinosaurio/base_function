# coding: utf-8
import os
print os.path.dirname(os.path.abspath(__file__))
temp= os.path.abspath(os.path.join(os.path.dirname(__file__),"../temp/HouseInfo"))
file= os.path.join(temp,'Qfang.py')
print file
with open(file,'r') as f:
    print f.read()