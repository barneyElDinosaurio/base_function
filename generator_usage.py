#-*-coding=utf-8-*-



# 生成器解析器

# coding: utf-8
from Queue import Queue

def generator_usage():
    g = (x for x in range(1000))
    #rint type(g)
    #print g
    #print g.next()
    while g:
        try:
            print g.next()
        except IOError:
            break
        else:
            print ' in else'
            return 0
        finally:
            print 'finanlly'
            return 1

def list_generator():
    l = [ x for x in range(1000)]
    print type(l)
    print l

def iter_function():
    a=[i for i in range(100)]
    b=iter(a)
    while True:
        try:
            print b.next()
        except StopIteration:
            print 'over'
            break

def key_function():
    d={'a':1,'z':2,'f':3,'g':9,'i':8}
    '''
    for i in d:
        print i
    '''

    for i in d.items():
    #for i in d.itervalues():
    #for i in d.iterkeys():
    #for i in d.iteritems():
        print i

def iter_usage():
    q=Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    q.put('END')

    def fetchdata():
        return q.get()

    for i in iter(fetchdata,'END'):
        print i



#iter_function()
#key_function()
#x = generator_usage()
#print x
#list_generator()
iter_usage()

    

def genlist():
    x = (i**2 for i in range(10))
    while 1:
        try:
            print next(x)
            # print x.next()
        except Exception as e:
            print e
            break

def gensquart(N):
    for i in range(N):
        yield i**3

def testcase():
    x = gensquart(10)
    '''
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    print x.next()
    '''
    while 1:
        try:
            print x.next()
        except StopIteration:
            print 'stop'
            break

    for i in gensquart(11):
        print i


class MyGenerator():
    def __init__(self,n):
        self.end=n
        self.current =-1
        self.content = []
        for i in range(self.end):
            self.content.append(i**3)
    def __iter__(self):
        return self

    def next(self):
         self.current=self.current+1
         return self.content[self.current]




def testcase2():
    obj = MyGenerator(10)
    '''
    print obj.next()
    print obj.next()
    print obj.next()
    print obj.next()
    '''
    for i in MyGenerator(10):
        print i


def main():
    genlist()
    # testcase()

main()