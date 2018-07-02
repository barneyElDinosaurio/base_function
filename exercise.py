#-*-coding=utf-8-*
import sys
print(bin(6))

print(len(bin(6)))
# 5的二进制 多少位 ？
#print len(5)
print(callable(1))

print(chr(65))
# A
if sys.version_info.major <3:
    print(cmp(3,4))
else:
    import operator
    print(operator.eq(3.0,3.00000))

# False
print(complex(1,2)==complex("1+2j"))
#True