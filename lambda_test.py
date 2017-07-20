# -*-coding=utf-8-*-
#lambdah函数的使用
def lambda_test(n):
    return lambda s: s + n

def testcase1():
    k = lambda_test(5)
    print k(4)
    print k(9)
    l = lambda x: x * x
    y = l(8)
    print y

def multipliers():
  return [lambda x : i * x for i in range(4)]

print [m(2) for m in multipliers()]
for i in multipliers():
    print i