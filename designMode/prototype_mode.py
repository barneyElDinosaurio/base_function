import copy

class A:
	def __init__(self):
		self.x=10
		# self.y=20
		self.msg = 'msg'
class B(A):
	def __init__(self):
		A.__init__(self)
		self.y=20


	def __str__(self):
		return 'x : {} y: {}'.format(self.x,self.y)

a=A()
b=B()
c=b
# c=copy.deepcopy(b)
# print(b)
print([str(i) for i in [b,c]])
print([id(i) for i in [b,c]])

b.y=30

print('b',b)
print('c',c)