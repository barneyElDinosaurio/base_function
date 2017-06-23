# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
你我金融的笔试题
'''
def exchange():
    a=10
    b=20
    a,b=b,a
    print a,b

def f1(*arg):
    for i in arg:
        print i

def f2(**args):
    for k in args:
        print "Key : %s value: %s" %(k,args[k])

def list_test(x,l=[]):
    for i in range(x):
        l.append(i*i)
        print l

def test_list_case():
    f1(1,'h',2)
    f2(h='help',o='option')

    list_test(4)
    list_test(5)

'''
a=1
def address(a):
    print "fun_in a",id(a)
    a=2
    print "remount a ", id(a),id(2)

print "fun out ", id(a),id(1)
address(a)
print a
'''

class ObjectCreator(object):
    pass

def main():
    #exchange()
    print ObjectCreator


if __name__=='__main__':
    main()

