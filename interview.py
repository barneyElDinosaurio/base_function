# -*-coding=utf-8-*-
import random
import time,copy
import datetime

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
你我金融的笔试题
'''
def exchange():
    a=10
    b=20
    a,b=b,a
    print a,b

def f1(*arg):
    for i in arg:
        print i

def f2(**args):
    for k in args:
        print "Key : %s value: %s" %(k,args[k])

def list_test(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print l
        print id(l)

def test_list_case():
    f1(1,'h',2)
    f2(h='help',o='option')



'''
a=1
def address(a):
    print "fun_in a",id(a)
    a=2
    print "remount a ", id(a),id(2)

print "fun out ", id(a),id(1)
address(a)
print a
'''

class ObjectCreator(object):
    pass
def foot(self):
    print "foot!!"
class ObjectCreator2():
    def foox(self):
        print "in obj2 foo"


def foo1(obj):
    print obj,'call'


class Test1():
    def help(self):
        print "in side"

def dynamic_class(name):
    if name=='foo':
        class foo():
            def __init__(self):
                print "foo"
        return foo
    else:
        class nobody():
            def __init__(self):
                print "nobody"
        return nobody

def testcase():
    x=dynamic_class('foo1')
    print x
    obj=x()
    print obj

def tesecase2():
    #exchange()
    print ObjectCreator
    foo1(ObjectCreator)
    print hasattr(ObjectCreator,'new_func')
    ObjectCreator.new_func=foo1('x')
    print hasattr(ObjectCreator,'new_func')
    #ObjectCreator.new_func('x')
    print hasattr(Test1,'help')
    testcase()
    print type(ObjectCreator)
    a=type('ObjectCreator',(),{})
    print a
    b=type('ObjectCreator2',(),{'foot':foot})
    print b
    c=b()
    #c.foox()
    print hasattr(b,'foox')
    #返回的是True
    c.foot()

class base_for_method():
    def foo(self):
        print "under base"

class method_test(base_for_method):

    def normal(self,x):
        print "Nornal method %s" %x

    @staticmethod
    def static_method(x):
        print 'Static method %s' %x
    @classmethod
    def class_method(cls,x):
        print "Class method %s %s" %(cls,x)


def testcase2():
    obj=method_test()
    obj.normal('x')
    obj.static_method('x')
    obj2=method_test()
    obj.class_method('x')
    method_test.static_method('jj')

class class_var():
    name='aaa'
    lover=[]

def testcase3():
    a=class_var()
    b=class_var()
    print a.name
    print b.name
    b.name='xxx'
    print b.name
    print class_var.name

    a.lover.append('1')
    a.lover.append('2')
    print a.lover
    print b.lover
    print class_var.lover
    obj=base_for_method()
    print isinstance(obj,method_test)

def testcase4():
    class line_test():
        first='Li'
        def __init__(self):
            self.name='yong'
            self._foo='ni hao'
    obj=line_test()
    print obj.first
    print obj.name
    print obj._foo

def testcase5():
    a=[1,2,3]
    b=(1,2,3)
    c={'a':'apple','b':'banana','c':'cat'}
    print "a=%s" % c
    f1('a','b','c','d')

def testcase6():
#单例,不太懂.回去继续研究
    class Sington(object):
        def __new__(cls, *args, **kwargs):
            if not hasattr(cls,'_instance'):
                org=super(Sington,cls)
                cls._intance=org.__new__(cls,*args,**kwargs)
            return cls._intance

    class MyObject(Sington):
        a=1
    obj=MyObject()
    print obj.a
    print obj

    obj2=MyObject()
    print obj2

def testcase7():
    a=[1,2,3,4,5,6]
    b=filter(lambda x:x>4,a)
    print b

    c=map(lambda x:x*x,a)
    print c

    d=reduce(lambda x,y:x*y,a)
    print d

def testcase8():
    age=10
    print age.__class__
    print age.__class__.__class__
    class Obj_Cls(object):
        pass
    print Obj_Cls.__class__.__class__


def testcase9():
    name='kingOfflight'
    print name.startswith('kn')

def testcase10():
    x=1
    a=(lambda t:(t for _ in xrange(10)))(x)
    b=[1,2,3,4,5](2)

    print list(a)
    print b

def testcase11():
    d=globals()
    print d


def check_time(func):
    def wrapper():
        #start=datetime.datetime.now()
        start=time.clock()
        func()
        use=(time.clock()-start)
        print use
        if use>1.0:
            print "bad"
        else:
            print "good"

    return wrapper

@check_time
def run_time():
    t=random.random()
    print t
    time.sleep(t*2)

def testcase12():
    run_time()


def testcase13():
    jack=['name','id',['male','math']]
    #tom=jack[:]
    #anny=list(jack)
    lily=jack
    tom=copy.deepcopy(jack)
    anny=copy.deepcopy(jack)
    print id(jack)
    print id(tom)
    print id(anny)
    print jack
    print tom
    print anny

    jack.append('married')
    jack[2].append('china')
    print jack
    print tom
    print anny

    if jack is lily:
        print "same"
    else:
        print "diff"
# 快速查找list中某个元素
def search_item(item,target):
    loc = item.index(target)
    return loc
def main():
    # testcase13()
    l = [2,1,33,2,11,22,99]
    print search_item(l,99)
if __name__=='__main__':
    main()

