#-*-coding=utf-8-*-
import math
#计算N的阶乘
import sys


def factorial(N):
    ret = 1
    for i in range(1,N+1):
        ret = ret*i

    return ret

#计算N的阶乘
def factorial_generator(N):
    ret = 1
    for i in range(1,N+1):
        ret = ret*i
        yield ret


# 排列 从n个中选出x个
def permutations(x,n):
    return factorial(n)/factorial(n-x)


# 组合 从n个中选出x个组合:
def combination(x,n):
    return permutations(x,n)/factorial(x)


def yield_calc(rate, money):
    return rate * money / 365 / 100


def fv():
    for i in range(1, 8):
        rise = (1.1 ** i - 1) * 100
        print("%d day's raise is %.2f" % (i, rise))

    for i in range(1,10):
        rise = 1.01**i
        print(rise)

    print(math.log(2,1.01))

def fv_yield(n):
    for i in range(1,n):
        rise=1.01**i
        yield rise




#c = yield_calc(3.65, 1000000)
#print(c)

#print(round(17.955, 2))
def percentage(a,b):
    print((a-b)*1.00/b*100)



def validation():
    for i in factorial_generator(10):
        print(i)

    print(permutations(2,6))
    print(combination(2,6))

def value_large():
    m = sys.maxint
    print(type(m))
    m=m+1
    print(m)
    w  = math.log(m,2)
    print(w)
    print(2**w)
def main():
    #percentage(0.195,0.185)
    #print(factorial(5))
    #validation()
    #fv()
    # fv_g=fv_yield(100)
    # print(fv_g.next())
    value_large()

def ops_test(n):
    print(n)
    return n

# run left then right
x = ops_test(2) + ops_test(5):

main()