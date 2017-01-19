# -*-coding=utf-8-*-
__author__ = 'Rocky'
import dis
sBuf=[0]*16
cur=0
def sPush(n):
    global cur
    if cur>15:
        print "Stack is full"
    else:
        sBuf[cur]=n
        cur=cur+1
        print cur
def sPop():
    global cur
    if cur<1:
        print "Stack is empty"
    else:
        sBuf[cur]=0
        cur=cur-1
        print cur
def main():
    sPop()
    sPush(1)
    sPush(2)
    sPush(3)
    print cur
main()
dis.dis(main)