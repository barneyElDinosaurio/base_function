# -*-coding=utf-8-*-
__author__ = 'Rocky'
import json
a=[1,2,3,4]
b=[54,3,2,1,2]
c=a+b
print c
d=list(set(c))
print d


urlss = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,6,1)]
#print urlss
for i in urlss:
    print i

record=[json.loads(line) for line in open('json.txt')]
print record
print '\n'
'''
for line in open('json.txt'):
    print line
    print "\n"
'''

def getCount(strings):
    counts={}
    for x in strings:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts
recordx=['a','b','c','a','b']
count=getCount(recordx)
print count['a']

