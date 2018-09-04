# -*-coding=utf-8-*-
__author__ = 'Rocky'
import os


def eval_test():
    exp = "2*10"
    result = eval(exp)
    print(result)

    a = input("Please input a exp:\n")
    t = eval(a)
    #这个时候如果输入了 os.system("dir") 就可以看到系统的目录文件
    print(t)


eval_test()