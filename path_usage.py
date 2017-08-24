<<<<<<< HEAD
# coding: utf-8
import os
print os.path.dirname(os.path.abspath(__file__))
temp= os.path.abspath(os.path.join(os.path.dirname(__file__),"../temp/HouseInfo"))
file= os.path.join(temp,'Qfang.py')
print file
with open(file,'r') as f:
    print f.read()
=======
import os
print os.path.dirname(os.path.abspath("__file__"))
print os.path.pardir
print os.path.join(os.path.dirname("__file__"),os.path.pardir)
print os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
>>>>>>> origin/master
