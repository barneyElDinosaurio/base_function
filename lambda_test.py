# -*-coding=utf-8-*-
#lambdah函数的使用
def lambda_test(n):
    return lambda s: s + n


k = lambda_test(5)
print k(4)
print k(9)
l = lambda x: x * x
y = l(8)
print y
