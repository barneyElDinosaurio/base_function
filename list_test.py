# -*-coding=utf-8-*-
__author__ = 'Rocky'
a=[1,2,3,4]
b=[54,3,2,1,2]
c=a+b
d=list(set(c))
print d

urlss = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,6,1)]
#print urlss
for i in urlss:
    print i
