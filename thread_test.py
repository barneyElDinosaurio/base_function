import thread
from time import sleep,ctime
def loop1():
	print "sart %s " %ctime()
	print "start in loop1"
	sleep(3)
	print "end %s " %ctime()

def loop2():
	print "sart %s " %ctime()
	print "start in loop2"
	sleep(6)
	print "end %s " %ctime()


def main():
	print "start at main"
	loop1()
	loop2()
	print "end at main"

if __name__=="__main__":
	main()
	
