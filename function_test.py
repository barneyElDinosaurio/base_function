import os
def getData(name,times):
    print "Your name is", name," Times is :",times

def getData(name):
    print "Your name is", name," Times is : None"


def path_function():
    print os.getcwd()

def print_fun():
    a=1
    #print '%d100/%\n' %a
    print "a values is ",a,"%"

def loopTest():
    for i in range(-9,10,1):
        print i
#getData('Rocky',1000)
#wrong!

#path_function()
#print_fun()
loopTest()