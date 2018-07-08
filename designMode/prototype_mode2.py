import copy
class Book:
	x='init'
	def __init__(self):
		self.a=0
		self.b=None


	def show(self):
		print(self.__dict__)

b = Book()
print('__dict__ content: ')

b.show()

b.c = 0

print('__dict__ content: ')
b.show()

d={'a':1,'b':2}
print(d)
x={1:1,2:2,3:3}
print(x)
d.update(x)
print(d)


class NewBook:
	def __init__(self,name,price,**rest):
		self.name = name
		self.price = price
		self.__dict__.update(rest)

	def __str__(self):
		t=[]
		for k,v in self.__dict__.items():
			s = '{} = {};\n'.format(k,v)
			t.append(s)
		
		return ''.join(t)


nb = NewBook(name="Worf", price=10, release='2018', publisher='RMB')
print(nb)


def func(**arg):
	for k,v in arg.items():
		print(k,v)


func(a='apple', b='banana', c='cat')


class ProtoType:
	def __init__(self):
		self.obj = None

	def register(self, obj):
		self.obj = obj

	def clone(self,**attr):
		# clone_obj = self.obj
		# if not use deepcopy , when clone_obj change , obj will be change as well.
		clone_obj =copy.deepcopy(self.obj)
		clone_obj.__dict__.update(attr)

		return clone_obj

p = ProtoType()
p.register(nb)
my_book = p.clone(year='2018',sex='male')
print(my_book)
print(nb)
