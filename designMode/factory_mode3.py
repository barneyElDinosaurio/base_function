from enum import Enum

PizzaProgress = Enum('PizzaProgressTag','queued preparation baking ready')
print(PizzaProgress.queued)

class A(object):

	def foo(self):
		print('hello',self)

	@classmethod
	def foo1(cls):
		print('hello',cls)
def testcase():
	a=A()
	b=A()
	a.foo()
	a.foo1()

class Pizza:
	def __init__(self,builder):
		self.garlic = builder.gralic
		self.extra_cheese = builder.extra_cheese

	def __str__(self):

		garlic = 'yes' if self.garlic else 'no'
		cheese = 'yes' if self.extra_cheese else 'no'
		return 'Pizza: garlic :{}, cheese : {}'.format(garlic,cheese)


	class PizzaBuilder:
		def __init__(self):
			self.garlic=None
			self.extra_cheese=None


		def add_gralic(self):
			self.gralic=True
			return self

		def add_cheese(self):
			self.extra_cheese=True
			return self

		def build(self):
			return Pizza(self)



def main():
	print(Pizza.PizzaBuilder().add_gralic().add_cheese().build())

main()