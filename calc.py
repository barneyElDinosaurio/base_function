#-*-coding=utf-8-*-

#计算N的阶乘
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


def test1():
    for i in range(1, 6):
        rise = (1.1 ** i - 1) * 100
        print "%d day's raise is %.2f" % (i, rise)


#c = yield_calc(3.65, 1000000)
#print c

#print round(17.955, 2)
def percentage(a,b):
    print (a-b)*1.00/b*100



def validation():
    for i in factorial_generator(10):
        print i

    print permutations(2,6)
    print combination(2,6)

def main():
    #percentage(0.195,0.185)
    #print factorial(5)
    validation()

main()