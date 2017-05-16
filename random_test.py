__author__ = 'rocky'
import random
# list=[1,2,3,4,5]
#print list[2]

list = []
for i in range(536870911):
    list.append(random.random())

print len(list)
