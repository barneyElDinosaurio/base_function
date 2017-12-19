import numpy as np
import math,time
# import matplotlib.pyplot as plt
from toolkit import timecal,loop_test

def numpysum(n):
    a = np.arange(n)
    b = np.arange(n)
    c = a + b
    return c

def testcase1():
    x = numpysum(20)
    print x
    d = np.array([1, 2, 34, 5])
    print d
    e = d.tolist()
    print e

    f = e
    g = np.array(f)
    print g

def testcase2():
    np.random.seed(2000)
    y=np.random.standard_normal((20,2))
    print y
    print type(y)

def testcase3():
    x=range(0,50)

    #x=x.map(lambda t:t*1.00/3.14)
    x=map(lambda t:t/3.14,x)
    #x=result(x)
    print x
    y=[math.sin(i) for i in x]
    plt.figure(1)
    plt.plot(x,y,'o',label='sin(x)')
    plt.grid()
    plt.show()


def testcase4():
    n=10
    x=np.arange(n)
    y1=np.random.uniform(0.5,1,n)
    y2=np.random.uniform(0.5,1,n)
    #print data.mean()
    #print data
    plt.figure(figsize=(9,6))
    plt.bar(x,y1,width=0.35,facecolor='lightblue',edgecolor='white')
    plt.bar(x+0.35,y2,width=0.35,facecolor='yellowgreen',edgecolor='white')
    plt.grid()
    plt.title("Bar1")
    for xn,yn in zip(x,y1):
        plt.text(xn+0.35,yn+0.05,'%.2f' %yn,ha='center',va='bottom')
    for xn2,yn2 in zip(x,y2):
        plt.text(xn2+0.6,yn2+0.05,'%.2f' %yn,ha='center',va='bottom')

    plt.ylim(0,1.25)
    plt.xlabel("number")
    plt.ylabel("uniform")
    plt.show()


def testcase5():
    x=np.arange(101)
    y=x.cumsum()
    print y
    print len(y)

def perf_compare():
    i=[x for x in xrange(10000000)]
    start=time.clock()
    for ii in i:
        k=math.sin(ii)
    end=time.clock()
    print "Time use:", end-start

    np_i=np.array(i)
    start=time.clock()
    np.sin(np_i)
    end=time.clock()
    print "numpy time used : ", end-start

@timecal
def python_multi(n):
    a= range(n)
    b= range(n)
    c=[]
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**3)
    return c

@timecal
def np_multi(n):
    return np.arange(n)**2+np.arange(n)**3

def base_type():
    a = np.arange(10)
    print a
    print 'a type {}'.format(type(a))
    print a.shape
    print a.dtype
    b = np.arange(0,10,0.5)
    print b
    zero_array = np.zeros(20)
    print zero_array

    a1 = np.array(range(20))
    print 'a1 is ',a1
    print a1[-1]
    print 'revert ',a1[::-1]
    b1 = np.arange(24)
    b2 = b1.reshape(2,3,4)
    print 'b1',b1
    print 'b2',b2


@loop_test
def Qscore():
    x=np.random.randn(1000).mean()
    print 'function x is',x
    return x


def main():
    #testcase4()
    # perf_compare()
    
    # python_multi(10000)
    # np_multi(10000)
    base_type()
    # x=Qscore()
    # print 'qcore x is',x

main()