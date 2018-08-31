# -*-coding=utf-8-*-
import random
import Queue
import time
import threading

q = Queue.Queue()

t_count = 16
start = time.time()


def divide_task(start, end, q):
    count = 0
    for i in range(start, end):
        count = count + random.randint(1, 10)
    print('count >>>>{}'.format(count))
    q.put(count)


def start_run():
    task_number = 4
    each_count = t_count / task_number
    thrd = []
    for i in range(task_number):
        t = threading.Thread(target=divide_task, args=(i, i + each_count, q,))
        thrd.append(t)

    for t in thrd:
        t.start()

    for t1 in thrd:
        t1.join()
    sum = 0

    while not q.empty():
        sum = sum + q.get()

    print('Total >>>>>'.format(sum))


end = time.time()

start_run()


print('time used: ',end-start)

