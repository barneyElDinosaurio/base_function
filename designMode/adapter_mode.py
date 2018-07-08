class Computer:
	
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return 'This is {} Computer'.format(self.name)

	def execute(self):
		print('execute a program')


class Human:
	
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return 'This is {} Computer'.format(self.name)

	def speak(self):
		print('speak a work')

class Piano:
	
	def __init__(self,name):
		self.name = name

	def __str__(self):
		return 'This is {} Computer'.format(self.name)

	def play(self):
		print('play a song')


class Adapter:

	def __init__(self, obj, adapter_name):
		self.obj = obj
		self.__dict__.update(adapter_name)


	def __str__(self):
		return str(self.obj)
		# return self.obj
# obj = Computer('NVIDIA')
# print(obj)

def main():
	obj = [Computer('Dell')]
	piano = Piano('Yamaha')
	human = Human('Joy')

	obj.append(Adapter(piano,dict(execute=piano.play)))
	obj.append(Adapter(human,dict(execute=human.speak)))

	for i in obj:
		# print(i)
		# print(i.__dict__)
		i.execute()
		print(i)


main()



