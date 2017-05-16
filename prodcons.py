# -*-coding=utf-8
from Queue import Queue
from random import randint
from MyThread import MyThread
from time import sleep


def queue_test(q):
    #q=Queue(10);
    for i in range(10):
        temp = randint(1, 10)
        print temp
        q.put("number:", temp)
        print "size of queue is %d" % q.qsize()


def writeQ(q, i):
    print "producter object for Q"
    data = randint(1, 10)
    #print "data is %d" %data
    q.put(i, 1)
    print "size now in producter is %d" % q.qsize()


def readQ(q):
    print "consumer object for Q"
    data = q.get(1)
    print data
    print "now after consume Q size is %d" % q.qsize()


def writer(q, loop):
    for i in range(loop):
        writeQ(q, i)
        sleep_time = randint(1, 3)
        sleep(sleep_time)


def reader(q, loop):
    for i in range(loop):
        readQ(q)
        sleep_time = randint(2, 5)
        sleep(sleep_time)


funcs = [writer, reader]
nfuncs = len(funcs)


def area_test(a):
    a = a * 10


def main():
    '''
    a=2
    print "a=%d" %a
    area_test(a)
    print "a now is a= %d" %a

    q=Queue(10);
    print "main q size %d" %q.qsize()
    queue_test(q)
    print "after function q size %d" %q.qsize()
    '''
    threads = []
    q = Queue(10)
    loop = 10
    for i in range(nfuncs):
        t = MyThread(funcs[i], (q, loop))
        threads.append(t)

    for i in range(nfuncs):
        threads[i].start()

    '''
    for i in range(nfuncs):
        threads[i].join()

    '''

#print "end of main"

if __name__ == "__main__":
    main()
