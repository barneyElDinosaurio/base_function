# coding: utf-8
import logging
def case1():
    try:
        print 'try'
        r =  int('a')
        #r =  int('a')
        print 'result is ',r
    except ZeroDivisionError as e:
        print 'exception ',e
    except IOError as e:
        print 'exception',e
    #except ValueError as e:
        #print 'exception:::' , e
        #logging.exception(e)
    else:
        print 'in else'
    finally:
        print 'finally'

    print 'end'

class Fooerror(ValueError):
    pass

def case2():
    a='0q'
    n=int(a)
    if n==0:
        raise Fooerror('foo invalid : %s' %a)
    return 10/n

#case1()
#case2()