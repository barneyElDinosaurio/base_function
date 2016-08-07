#-*-coding=utf-8-*-
# classmethod 和 staticmethod 的用法
__author__ = 'rocchen'

class Hero():

    @staticmethod
    def sayHello():
        print "hello in static"

    @classmethod
    def sayHello_cls(cls):
        if cls.__name__=="Girl_Hero":
            print "Girl_Hero in classmethod"
        elif cls.__name__=="Boy_Hero":
            print "Boy_Here in classmethod"

class Girl_Hero(Hero):

    def foo(self):
        print "in Girl"

class Boy_Hero(Hero):

    def foo(self):
        print "in Boy"
'''
test=Girl_Hero()
test.sayHello_cls()
test.sayHello()

test1=Boy_Hero()
test1.sayHello_cls()
test1.sayHello()
'''

#factory mode
class worker():
    def pick(self):
        print "Pick up"
    def drop(self):
        print "Drop down"

class Phone_worker(worker):
    def work_fun(self):
        print "calling"

class Wath_worker(worker):
    def work_fun(self):
        print "watching"

class PC_worker(worker):
    def work_fun(self):
        print "Typing"

class Factory_Work():
    @classmethod
    def get_fun(cls,worker_name):
        if worker_name=="phone":
            return Phone_worker()
        elif worker_name=="watch":
            return Wath_worker()
        elif worker_name=="PC":
            return PC_worker()


a=Factory_Work.get_fun("phone")
#b=a.get_fun("PC")
a.work_fun()
