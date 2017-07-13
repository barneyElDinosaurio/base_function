# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import os

def fork_case():
    print "Process %s start " %os.getpid()
    pid=os.fork()

    if pid==0:
        print "i am child process. and my parent pid is %s " %os.getpid()
    else:
        print "i am parent process %s, and create my child process %s" %(os.getpid,pid)


def main():
    fork_case()
main()