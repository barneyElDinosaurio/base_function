import numpy as np


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
    