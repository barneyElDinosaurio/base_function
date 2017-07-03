#-*-coding=utf-8-*-
import logging


def get_parameter(func):
    print "IN GET PARAMETER"

    def new_func():
        print "inside new func"
        return func()

    print "END GET PARAMETER"
    return new_func


@get_parameter
def show_function():
    print "SHOW Function"
    return "HELLO"


# a=show_function
#a()
#get_parameter()
#a=show_function()
#print a

#演示2个装饰器同时使用
def add_br(func):
    #print '<br>',

    def wrapper():
        print "br"
        return '<br>'+func()+'</br>'
    return wrapper

def add_header(func):
    def wrapper():
        print "header"
        return "<header>" +func()+ '</header>'
    return wrapper

@add_header
@add_br
def sayHelloWorld():
    return "Hello world！"


def deco1(func):
    def wrapper(arg1,arg2):
        print "Start"
        func(arg1,arg2)
        print "End"
    return wrapper

@deco1
def args_deco_test(x1,x2):
    print "first args is %s . Second args is %s." %(x1,x2)


def multi_args(func):
    def wrapper(*args,**kwargs):
        print "start"
        func(*args,**kwargs)
        print "end"
    return wrapper

@multi_args
def deco_multi_arg(*args,**kwargs):
    for i in args:
        print "args : %s" %i

    for k in kwargs:
        print "key=" ,k
        print 'value=',kwargs[k]
    print "end in main"



def deco_rocky(name):
    print "deco_rocky: ",name
    def sub_function(func):
        print "sub function"
        def wrapper(args1,args2):
            print "in wrapper"
            func(args1,args2)
            print "end of wrapper"
        return wrapper
    return sub_function

@deco_rocky("Dinesh")
def foo_focky(arg1,arg2):
    print "In foo_rocky"
    print "arg1: ",arg1
    print "arg2: ",arg2
    print "End of foo_rocky"

def main():
    print sayHelloWorld()
    #print "Morning"
    #args_deco_test('one','two')
    #deco_multi_arg('args1','args2','args3','args4',name="Rocky",sex="Female")
    #foo_focky('HHH','Mars')

if __name__ == "__main__":
    #logging.info("Test")
    #print "Test"
    #show_function()
    #sayHello()
    main()