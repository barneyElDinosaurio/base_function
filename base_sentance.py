# -*-coding=utf-8-*-
__author__ = 'xda'
import urllib

def bool_demo():
    a=1
    ret = bool(a)
    print(ret)
    b=None
    ret2= bool(b)
    print(ret2)

def exception_demo():
    try:
        #Normal execution block
        open('data.cfg', 'r')
    except urllib.UnknownHandler as e:
        #Exception A handle
        print("can't find")
    except urllib.URLError as e:
        #Exception B handle
        print("still error")
    except urllib.UnknownHandler as e:
        #Other exception handle
        print("error")
    else:
        #if no exception,get here
        print("open")
    finally:
        print("finally")

    import six
    print(six.PY2)


def if_else_test():
    name = "Rockyj"
    passwd = "rocky" if name in ['Rocky', 'Chen', "Hello"] else "fixed"
    print(passwd)


def _random(n=13):
    from random import randint

    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    return str(randint(start, end))

bool_demo()
# if_else_test()
# print(_random(17))