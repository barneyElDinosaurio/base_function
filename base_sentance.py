# -*-coding=utf-8-*-
__author__ = 'xda'
import urllib2

try:
    #Normal execution block
    open('data.cfg', 'r')
except urllib2.UnknownHandler as e:
    #Exception A handle
    print("can't find")
except urllib2.URLError as e:
    #Exception B handle
    print("still error")
except urllib2.UnknownHandler as e:
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


if_else_test()
print(_random(17))