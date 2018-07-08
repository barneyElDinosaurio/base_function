#-*-coding=utf-8-*-
'''
赌博
'''
import random
import numpy as np
import matplotlib.pyplot as plt
def gamble_test(cash):
	
	counts=[]
	for i in range(1000):

		count = 0
		current_cash = cash
		while current_cash >0:
			count+=1
			x=random.randint(1,10)
			# print(x)
			pay = (1 if x >5 else -1)
			current_cash = current_cash + pay

		# print('count',count)
		counts.append(count)
	print(max(counts)  	)
	return float(sum(counts))/100.0

print(gamble_test(1))
# x = range(1,100)
# result = [gamble_test(i) for i in range(1,100)]
# print(result)
# d = np.array(result)
# print(d.mean())
# print(d.std())
# plt.plot(x,result)
# plt.show()
