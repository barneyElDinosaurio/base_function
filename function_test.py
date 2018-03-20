import os
import pprint
from functools import partial

def getData(name, times):
    print "Your name is", name, " Times is :", times


def getData(name):
    print "Your name is", name, " Times is : None"

def path_function():
    print os.getcwd()


def print_fun():
    a = 1
    # print '%d100/%\n' %a
    print "a values is ", a, "%"
    print 'a values is %d%%' %a


def loopTest():
    for i in range(-9, 10, 1):
        print i

def sayHi(x,name):
    return x+name

def return_case():
    x=1
    y='hello'
    return x,y

def get_return_case():
    x,y=return_case()

    print x
    print y


def print_case():
    a=[1,2,3,'hello',['w',12,'d']]
    pprint.pprint(a)

def os_system():
    # os.system('notepad.exe')
    os.system('shutdown -h now')

def foo(x):

    def zoo(x,y):
        return x+y

    return zoo

# def main():
#     p=partial(sayHi,name='Rocky')
#     print p('Chen')
#     print p('Li')
#     print p('Peng')
#     print p('Luo')
#     get_return_case()

import getpass
def getpass_function():
    name=raw_input('input your name:\n')
    print getpass.getuser()
    password=getpass.getpass('input your password:\n')
    print 'name {0} ; password {1}'.format(name,password)


def many_func():
    f_name = [path_function,print_fun,loopTest]
    for fun in f_name:
        fun()

def call_back_case1(x):
    return x*2

def call_back_case2(x):
    return x*4

def call_back_demo(k,fun):
    return 1+fun(k)


def main():
    # getData('Rocky',1000)
    #wrong!

    # getData('Rocky')
    #path_function()
    #print_fun()
    #loopTest()
    #print_case()
    # os_system()
    # a = foo(100)
    # b=a(9,9)
    # print b
    # getpass_function()
    # many_func()
    print call_back_demo(5,call_back_case1)
    print call_back_demo(5,call_back_case2)

if __name__ =='__main__':
    main()