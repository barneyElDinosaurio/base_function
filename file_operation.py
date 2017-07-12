# -*-coding=utf-8-*-
__author__ = 'Rocky'
import os, re


def func():
    cwd = os.getcwd()
    p = re.compile('\.txt')
    print cwd
    for dirpath, dirname, filename in os.walk(cwd):
        # print dirpath,dirname,filename
        #print dirpath
        print dirname
        print type(filename)
        if filename is not None:
            for i in filename:
                #if filename is not None:

                if p.search(i):
                    os.remove(os.path.join(dirpath, i))


def testcase1():
    i = "memory"
    sub_folder = os.path.join(os.getcwd(), i)
    print sub_folder


def testcase2():
    #read/readline/readlines
    f1=open('data.cfg','r')
    r1=f1.read()
    print 'type of r1 ', type(r1)
    print 'content of r1 ', r1

    r2=f1.readlines()

    print 'type of r2 ', type(r2)
    print 'content of r2 ', r2

    '''
    print 'type of r1 ', type(r1)
    print 'content of r1 ', r1
    '''

def main():
    testcase2()
if __name__ == '__main__':
    main()