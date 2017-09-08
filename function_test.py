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
def main():
    p=partial(sayHi,name='Rocky')
    print p('Chen')
    print p('Li')
    print p('Peng')
    print p('Luo')
    get_return_case()

def print_case():
    a=[1,2,3,'hello',['w',12,'d']]
    pprint.pprint(a)

def os_system():
    os.system('notepad.exe')

# getData('Rocky',1000)
#wrong!

#path_function()
#print_fun()
#loopTest()
#print_case()
print os_system()