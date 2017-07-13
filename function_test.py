import os
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


def loopTest():
    for i in range(-9, 10, 1):
        print i

def sayHi(x,name):
    return x+name

def main():
    p=partial(sayHi,name='Rocky')
    print p('Chen')
    print p('Li')
    print p('Peng')
    print p('Luo')

main()

# getData('Rocky',1000)
#wrong!

#path_function()
#print_fun()
#loopTest()
