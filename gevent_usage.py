from gevent import monkey;	monkey.patch_socket()
import gevent

def f(n):
	for i in range(n):
		print gevent.getcurrent(),i
		gevent.sleep(0.1)

def main():
	g1=gevent.spawn(f,5)
	g2=gevent.spawn(f,5)
	g3=gevent.spawn(f,5)
	g4=gevent.spawn(f,5)
	g5=gevent.spawn(f,5)
	g1.join()
	g2.join()
	g3.join()
	g4.join()
	g5.join()


main()
