# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
#注意这里需要用object， 这样定义的class是新类，基于python3的
class base(object):
    def __init__(self):
        print "base constructor"

    def foo(self):
        print "base foo"


class base2():
    def __init__(self):

        print "base2 constructor"

    def foo(self):
        print "base2 foo"


class child(base):
    def __init__(self):
        super(child,self).__init__()
        print "child constuctor"
        #.__init__()

    def foo(self):
        #super(child,self).foo ()
        super(child,self).foo()
        #base.foo(self)
        print "child foo"

class child2(base):
    def __init__(self):
        base.__init__(self)

class child3(base):
    def __init__(self):
        super(child3,self).__init__()


#obj=child()
#obj.foo()
obj1=child2()
obj2=child3()