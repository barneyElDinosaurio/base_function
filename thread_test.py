import thread,threading,time,datetime
from time import sleep,ctime
def loop1():
	print "start %s " %ctime()
	print "start in loop1"
	sleep(3)
	print "end %s " %ctime()

def loop2():
	print "sart %s " %ctime()
	print "start in loop2"
	sleep(6)
	print "end %s " %ctime()


class MyThread(threading.Thread):
	def __init__(self,fun,arg,name=""):
		threading.Thread.__init__(self)
		self.fun=fun
		self.arg=arg
		self.name=name
		#self.result

	def run(self):
		self.result=apply(self.fun,self.arg)
	
	def getName(self):
		return self.name

	def getResult(self):
		return self.result

def fib(n):
	if n<2:
		return 1
	else:
		return fib(n-1)+fib(n-2)


def sum(n):
	if n<2:
		return 1
	else:
		return n+sum(n-1)	

def fab(n):
	if n<2:
		return 1
	else:
		return n*fab(n-1)


	
	

def single_thread():		
	print fib(12)		
	print sum(12)
	print fab(12)


def multi_thread():
	print "in multithread"
	fun_list=[fib,sum,fab]
	n=len(fun_list)
	threads=[]
	count=12
	for i in range(n):
		t=MyThread(fun_list[i],(count,),fun_list[i].__name__)
		threads.append(t)
	for i in range(n):
		threads[i].start()

	for i in range(n):
		threads[i].join()
		result= threads[i].getResult()
		print result
def fast():
	print "in fast"
	sleep(15)
	print "done in fast"

def slow():
	print "in slow"
	sleep(10)
	print "done in slow"

def wireteQ(queue):
	pass

def main():
	'''
	print "start at main"
	thread.start_new_thread(loop1,())
	thread.start_new_thread(loop2,())
	sleep(10)
	print "end at main"
	'''
	'''
	start=ctime()
	#print "Used %f" %(end-start).seconds
	print start	
	single_thread()
	end=ctime()
	print end
	multi_thread()
	'''
	#print "used %s" %(end-start).seconds 
	
	threads=[]
	f=[fast,slow]
	l=len(f)
	for i in range(l):
		t=MyThread(f[i],(),str(i))
		threads.append(t)
	
	for i in range(l):
		threads[i].start()

	for i in range(l):
		#pass
		threads[i].join()
		print threads[i].getName()
	print "Done on main"
	exit()

main()
	
'''		
if __name__=="__main__":
	main()
'''
