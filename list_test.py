# -*-coding=utf-8-*-
__author__ = 'Rocky'
import json
from Queue import Queue
#from multiprocessing import Queue

def case1():
    a = [1, 2, 3, 4]
    b = [54, 3, 2, 1, 2]
    c = a + b
    print c
    d = list(set(c))
    print d

    urlss = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1, 6, 1)]
    # print urlss
    for i in urlss:
        print i

    record = [json.loads(line) for line in open('json.txt')]
    print record
    print '\n'
    '''
    for line in open('json.txt'):
        print line
        print "\n"
    '''


def getCount(strings):
    counts = {}
    for x in strings:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts


def empty_test():
    my_list = [0, 0, 0, 0, 0, 0]
    if 0 in my_list:
        print 'empty'
        my_list = []
        print type(my_list)
    if len(my_list) == 0:
        print "None"


def modify_list():
    lst = list("IamRocky")
    print lst

    for i, strs in enumerate(lst):
        print "Index", i, "content", strs


def in_test():
    a = ['sam', 'disk', 'jacky', 'homeless']
    b = 'jacky'
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
    x = [[1, 2], [3, 4], [5, 6], [7, 8]]
    for i in x:
        # print i
        if 5 in i:
            x.remove(i)
    print x

def generator_list():
    g = (sum(i) for i in [(1,2,3),(4,5,6),(7,8,9)])
    h = [sum(i) for i in [(1,2,3),(4,5,6),(7,8,9)]]

    print type(g)
    print type(h)
    print g
    #print g.get(1)
    for i in g:
        print i
    print h

def iter_test():
    a=[1,2,3,4,5,6]
    i=iter(a)
    '''
    for x in i:
        print x
    print i
    '''
    while 1:
        try:
            print next(i)
            print 'while'
        except Exception,e:
            print e
            break
    print i

    while 1:
        try:
            print next(i)
            #不会有任何输出，因为你已经在上一个循环中迭代完成了，位置已经指向最后。
        except Exception,e:
            print e
            break
def rang_test():
    '''
    for v in range(1000000000000): #possible Memory Error
        if v == 2:
            break
    '''
    for v in xrange(100000): #fine
        if v == 2:
            break

def generator_test(a):
    #a=0
    i=0
    while i<a:

        yield i*i
        i=i+1


def use_generator():
    '''
    for i in generator_list(10):
        print i
    '''
    #x=generator_test(10)
    #print x

    for i in generator_test(10):
        print i

def cut_case():
    #y=[1,2,3,4,5,6]
    y=range(0,200)
    print y[:,0]


def iter_case2():
    q=Queue()
    org=['a','b','c','d','e','f','not see this']
    for i in org:
        q.put(i)
    for j in iter(q.get,'d'):
        print j


def mutebale():
    a=2
    print id(a)
    a=5
    print id(a)

    x='abc'
    y=x.replace('a','A')
    print x
    print y

def in_usage():
    l=range(100000)
    if 100000 in l:
        print "In"
    else:
        print "Not in"

def reversed_usage():
	s='Python'
	q=reversed(s)
	print q
	print type(q)
	print list(q)
	
def remove_list():
	l=[1,2,3,4,5]
	x=l.remove(1)
	print x
	print l
	
	x=l.pop(0)
	print x
	print l



def extendList(val, list=[]):
    list.append(val)
    return list

def extend_case():
    list1 = extendList(10)
    list2 = extendList(123,[])
    list3 = extendList('a')

    print "list1 = %s" % list1
    print "list2 = %s" % list2
    print "list3 = %s" % list3

    list = [ [ ] ] * 5
    print list
    print len(list)
    list[0].append(10)
    print list
    list[1].append(20)
    print list
    list.append(30)
    print list
def list_filter():
    l=[12,22,43,23,65,34,22,33,55,22,11,2,3,5,7]
    l1=l[2:8:2]
    print l1
    print id(l)
    print id(l1)
# in_test()
#delete_item_list()
#generator_list()
#iter_test()
#rang_test()
#use_generator()
#cut_case()
#iter_case2()
#mutebale()
#in_usage()
#case1()
#reversed_usage()
#remove_list()
list_filter()