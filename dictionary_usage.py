#-*-coding=utf-8-*-
import random

keys=[chr(i) for i in range(ord('A'),ord('Z')+1)]

print keys

values=[random.randint(0,100) for i in range(len(keys))]

print values

d=zip(keys,values)
print d
print type(d)
d1=dict(d)
print d1

k=sorted(d1.items(),key=lambda x:x[1],reverse=True)
print k



