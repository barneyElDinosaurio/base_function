# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
class FirstClass():
    def __init__(self):
        print "I am first class"

    def show_name(self):
        print self.__class__
class SecondClass():
    def __init__(self):
        print "I am second class"

    def show_name(self):
        print self.__class__

def select_class(choice):
    if choice==1:
        return FirstClass()

    else:
        return SecondClass()

obj=select_class(10)
print type(obj)
print id(obj)
obj.show_name()