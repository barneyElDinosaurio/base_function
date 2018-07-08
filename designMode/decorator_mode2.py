known = {0:0,1:1}

def fibonacci(n):
	print('current n {}'.format(n))
	# print('know : ',known)
	if n in known:
		return known[n]

	
	res = fibonacci(n-1)+fibonacci(n-2)
	known[n]=res

	return res

print(fibonacci(10))
# from timeit import Timer

# t =Timer('fibonacci(10)','from __main__ import fibonacci')
# print(t.timeit())

