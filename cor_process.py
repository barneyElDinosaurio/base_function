import time

def consumer():
	r=''
	while True:
		n = yield r
		if not n:
			return

		print('[Consumer] consuming %s ...' % n )
		time.sleep(2)
		r='200 OK'


def produce(c):
	c.next()
	n=0
	while n<5:
		n=n+1
		print('[Productor] Producing %s ...' %n)
		r=c.send(n)
		print('[Productor] Consumer return %s' %r)

	#c.close()

def main():
	c=consumer()
	#c.next()
	#c.next()
	produce(c)

main() 
