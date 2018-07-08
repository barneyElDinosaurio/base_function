class Publisher(object):
	def __init__(self):
		self.observers = []

	def add(self, obj):
		if obj not in self.observers:
			self.observers.append(obj)
		else:
			print('fail to add {}'.format(obj))

	def remove(self, obj):
		try:
			self.observers.remove(obj)
		except Exception as e:
			print(e)

	def notify(self):
		[i.notify(self) for i in self.observers]

class DefaultFormater(Publisher):

	def __init__(self, name):
		Publisher.__init__(self)
		self.name = name
		self._data = 0

	def __str__(self):
		return '{}:{} data={}'.format(type(self).__name__,self.name,self._data)

	@property
	def data(self):
		return self._data

	@data.setter
	def data(self, new_value):
		try:
			self._data = int(new_value)
			print('value change')
		except:
			print('error')
		else:
			self.notify()

	# def notify(self):

class HexFormater(object):

	def notify(self, publisher):
		print('{} : {} has data {}'.format(type(self).__name__,publisher.name,hex(publisher.data)))

class BinaryFormater(object):

	def notify(self, publisher):
		print('{} : {} has data {}'.format(type(self).__name__,publisher.name,bin(publisher.data)))		


def main():

	df = DefaultFormater('test1')
	print(df) 

	a = HexFormater()

	# print(df)
	df.add(a)
	# df.add(b)
	df.data=104
	print(df)
	b = BinaryFormater()
	df.add(b)
	print(df)
	df.data = 200


main()
