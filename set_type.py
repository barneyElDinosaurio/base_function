# -*-coding=utf-8-*-
def case1():
    s=set('helloworld')
    print s

    # f can't change
    f=frozenset('world!')
    print f
    if 'h' in s:
        print True
    if 'w' in f:
        print True

    s.add('world')
    s.add('w')
    s.add('w')
    s.update('123')
    print s
    try:
        f.add('k')
    except Exception as e:

        print e
case1()
