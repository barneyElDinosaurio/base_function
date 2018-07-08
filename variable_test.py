# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
全局变量的使用
'''
# import dis
sBuf=[0]*16
cur=0
def sPush(n):
    global cur
    if cur > 15:
        print("Stack is full")
    else:
        sBuf[cur] = n
        cur = cur + 1
        print(cur)


def sPop():
    global cur
    if cur < 1:
        print("Stack is empty")
    else:
        sBuf[cur] = 0
        cur = cur - 1
        print(cur)


def main():
    sPop()
    sPush(1)
    sPush(2)
    sPush(3)
    sPush(5)
    print(cur)
    print(sBuf)

main()
#dis.dis(main)
'''
#这个移位用太多时间了
a = 2 ** 10000000
print(a)
'''