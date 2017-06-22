# -*-coding=utf-8-*-
# classmethod 和 staticmethod 的用法
__author__ = 'rocky chen'


class Hero():
    '''
    this is the python doc test
    '''
    @staticmethod
    def sayHello():
        print "hello in static"

    '''
    will this effect ?
    '''
    @classmethod
    def sayHello_cls(cls):
        if cls.__name__ == "Girl_Hero":
            print "Girl_Hero in classmethod"
        elif cls.__name__ == "Boy_Hero":
            print "Boy_Here in classmethod"


h=Hero()
print h.__doc__
#h.sayHello()
Hero.sayHello()

class Girl_Hero(Hero):
    def foo(self):
        print "in Girl"


class Boy_Hero(Hero):
    def foo(self):
        print "in Boy"



test=Girl_Hero()
test.sayHello_cls()
test.sayHello()

test1=Boy_Hero()
test1.sayHello_cls()
test1.sayHello()


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
    def get_fun(cls, worker_name):
        if worker_name == "phone":
            return Phone_worker()
        elif worker_name == "watch":
            return Wath_worker()
        elif worker_name == "PC":
            return PC_worker()


class Person():
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    @property
    def p_name(self):
        return self.first_name + ' ' + self.last_name


'''
a=Factory_Work.get_fun("phone")
#b=a.get_fun("PC")
a.work_fun()
'''

person = Person("Jacky", "He")
print person.p_name
person.last_name = "HHHH"
print person.p_name

from abc import  abstractmethod,ABCMeta
class abc_abstract_test():
    __metaclass__=ABCMeta
    @abstractmethod
    def fun(self):
        '''

        :return:
        '''

class sub_class(abc_abstract_test):
    def getSize(self):
        print "Size"

    def fun(self):
        print "New here"


obj=sub_class()
obj.fun()
obj.getSize()

