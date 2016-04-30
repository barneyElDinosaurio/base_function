#-*-coding=utf-8
from Queue import Queue
from random import randint
from MyThread import MyThread
from time import sleep
def queue_test(q):
	#q=Queue(10);
	for i in range(10):
		temp=randint(1,10)
		print temp
		q.put("number:",temp)
		print "size of queue is %d" %q.qsize()

def writeQ(q):
	print "producter object for Q"
	data=randint(1,10)
	print "data is %d" %d
	q.put("temp",data)
	print "size now in producter is %d" %q.qsize()	

def readQ(q):
	print "consumer object for Q"
	data=q.get(1)
	print "now after consume Q size is %d" q.qsize()

def writer(q,loop)
	for i in range(loop):
		writeQ(q)
		sleep_time=randint(1,3)
		sleep(sleep_time)

def area_test(a):
	a=a*10

def main():
	a=2
	print "a=%d" %a
	area_test(a)
	print "a now is a= %d" %a

	q=Queue(10);
	print "main q size %d" %q.qsize()
	queue_test(q)
	print "after function q size %d" %q.qsize()

if  __name__=="__main__":
	main()
