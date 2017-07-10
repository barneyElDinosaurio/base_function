#-*-coding=utf-8-*-

import Queue

def task(name,work_queue):
    if work_queue.empty() :
        print "task %s is empty " %name
    while not work_queue.empty():
        count=work_queue.get()

        for x in range(count):
            print 'task %s is counting' %name
            print x

def main():
    q=Queue.Queue()
    count_list=[5,10,20,13]
    for i in count_list:
        q.put(i)

    tasks_list=[(task,'first',q),
                (task,'second',q)]

    for t,n,q_list in tasks_list:
        t(n,q_list)
        print "!"


main()