#-*-coding=utf-8-*-
import logging

'''
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

'''
# a=show_function
#a()
#get_parameter()
#a=show_function()
#print a

#演示2个装饰器同时使用
def add_br(func):
    #print '<br>',

    def wrapper():
        return '<br>'+func()+'</br>'
    return wrapper

def add_header(func):
    def wrapper():
        return "<header>" +func()+ '</header>'
    return wrapper

@add_header
@add_br
def sayHelloWorld():
    return "Hello world！"


def main():
    print sayHelloWorld()

if __name__ == "__main__":
    #logging.info("Test")
    #print "Test"
    #show_function()
    #sayHello()
    main()