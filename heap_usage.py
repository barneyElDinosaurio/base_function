import heapq,random
def basic_usage():
	h=[]
	heapq.heappush(h,10)
	print(h)
	heapq.heappush(h,1)
	print(h)
	heapq.heappush(h,0)
	print(h)
	heapq.heappush(h,3)
	print(h)
	heapq.heappush(h,6)
	print(h)
	heapq.heappush(h,7)
	print(h)
	heapq.heappush(h,11)
	print(h)
	heapq.heappush(h,9)
	print(h)
	heapq.heappush(h,7)
	print(h)
	heapq.heappush(h,2)
	print(h)
	p=heapq.heappop(h)
	print(h)
	print(p)
	
def heap_sort():
	l=[random.randint(0,100) for i in range(100)]
	print(l)
	h_l=heapq.heapify(l)
	print(type(h_l))
	print(l)
	print(type(l))
	'''
	m=heapq.heappop(l)
	print(m)
	print(l)
	'''
	while len(l)!=0:
		print(heapq.heappop(l))
	print('done')
#basic_usage()
heap_sort()