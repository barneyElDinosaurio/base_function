#-8-coding=utf-8-*-
class Base():
	name = 'Rocky'
	def __init__(self):
		self.foo = 'foo_value'

	def mydefine():
		print 'in foo'

class DelUsage():
	count =0

	def __init__(self):
		DelUsage.count=DelUsage.count +1
		print 'init class'
		print DelUsage.count

	def __del__(self):
		DelUsage.count=DelUsage.count-1
		print 'del class'
		print DelUsage.count

class Access():
	foo=1.2

class ChildAccess(Access):
	bar =20

def main():
	print Base.__dict__
	obj = Base()
	print dir(obj)
	print vars(Base).keys()
	print obj.__dict__
	print vars(obj)
	print dir(obj)

	a=DelUsage()
	b=DelUsage()
	c=DelUsage()
	#b=a
	#c=a
	del a
	del b
	del c
	print vars(Access)
	Access.foo = 2
	print vars(Access)
	ojb_access = Access()
	ojb_access.foo = 10
	print vars(Access)
	print vars(ojb_access)

	print Access.foo

	obj_child = ChildAccess()
	Access.foo = 99
	print obj_child.foo
	ojb_access.good = 'rocky'
	print ojb_access.__dict__



main()