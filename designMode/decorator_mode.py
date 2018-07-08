def fibonacci(n):
	print(n)
	return n if n in (0,1) else fibonacci(n-1)+fibonacci(n-2)



print(fibonacci(10))
# from timeit import Timer

# t =Timer('fibonacci(10)','from __main__ import fibonacci')
# print(t.timeit())