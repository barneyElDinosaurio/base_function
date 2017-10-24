# -*-coding=utf-8-*-
def case1():
    s=set('hello')
    print s
    f=frozenset('world!')
    if 'h' in s:
        print True
    if 'w' in f:
        print True

    s.add('world')
    s.add('w')
    s.add('w')
    s.update('123')
    print s
case1()
