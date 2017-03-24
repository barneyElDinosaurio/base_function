# -*-coding=utf-8-*-
__author__ = 'Rocky'
import json
def case1():
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


def empty_test():
    my_list=[0,0,0,0,0,0]
    if   0 in my_list:
        print 'empty'
        my_list=[]
        print type(my_list)
    if len(my_list)==0:
        print "None"

def modify_list():
    lst=list("IamRocky")
    print lst

    for i,strs in enumerate(lst):

        print "Index",i,"content",strs


def in_test():
    a=['sam','disk','jacky','homeless']
    b='jacky'
    if b in a:
        print b
    else:
        print "not there"
'''
Above are functions
'''
'''
recordx=['a','b','c','a','b']
count=getCount(recordx)
print count['a']
modify_list()
'''

def delete_item_list():
    x=[[1,2],[3,4],[5,6],[7,8]]
    for i in x:
        #print i
        if 5 in i:
            x.remove(i)
    print x

#in_test()
delete_item_list()