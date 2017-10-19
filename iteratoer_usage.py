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

x = generator_usage()
print x
#list_generator()