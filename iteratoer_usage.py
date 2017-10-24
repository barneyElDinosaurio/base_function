# coding: utf-8
def generator_usage():
    g = (x for x in range(1000))
    #rint type(g)
    #print g
    #print g.next()
    while g:
        try:
            print g.next()
        except IOError:
            break
        else:
            print ' in else'
            return 0
        finally:
            print 'finanlly'
            return 1

def list_generator():
    l = [ x for x in range(1000)]
    print type(l)
    print l

def iter_function():
    a=[i for i in range(100)]
    b=iter(a)
    while True:
        try:
            print b.next()
        except StopIteration:
            print 'over'
            break

def key_function():
    d={'a':1,'z':2,'f':3,'g':9,'i':8}
    '''
    for i in d:
        print i
    '''

    for i in d.items():
    #for i in d.itervalues():
    #for i in d.iterkeys():
    #for i in d.iteritems():
        print i

#iter_function()
key_function()
#x = generator_usage()
#print x
#list_generator()