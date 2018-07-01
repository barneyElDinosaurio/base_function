# coding: utf-8
import logging
def case1():
    try:
        print('try')
        r =  int('a')
        #r =  int('a')
        print('result is ',r)
    except ZeroDivisionError as e:
        print('exception ',e)
    except IOError as e:
        print('exception ',e)
    except ValueError as e:
        print('exception:::' , e)
    else:
        print('in else')
    finally:
        print('finally')

    print('end')

class Fooerror(ValueError):
    pass

def case2():
    a='0q'
    n=int(a)
    if n==0:
        raise Fooerror('foo invalid : %s' %a)
    return 10/n

def case3(a):
    try:
        if a<=0:
            raise ValueError('Data can not be negative')
        else:

            print('Run ????')
            # 因为有finally的存在，所以会打印run ？？？？ 但是后面的return不会返回a
            return a

    except ValueError as e:
        print(e)

    finally:
        print("In finally")
        return -1



# case1()
# case2()
print(case3(0))
print(case3(2))