from enum import Enum
State = Enum('state','new running sleeping restart zombie')
# print(state.new)
from abc import ABCMeta,abstractmethod

class Server(object):
	__metaclass__=ABCMeta
	@abstractmethod
	def __init__(self):
		pass

	def __str__(self):
		return self.name

	@abstractmethod
	def boot(self):
		pass

	@abstractmethod
	def kill(self):
		pass



class FileServer(Server):

	def __init__(self):
		self.name = 'FileServer'
		self.state = State.new

	def boot(self):
		self.state = State.running
		print('booting the {}'.format(self))

	def kill(self):
		self.state = State.zombie
		print('killing the {}'.format(self))

	def create_file(self,user,filename,permission):
		print('trying to create file {} with user {} with permission {}'.format(filename,user,permission))


	def status(self):
		print('current status is {}'.format(self.state))


class ProcessServer(Server):

	def __init__(self):
		self.name = 'ProcessServer'
		self.state = State.new

	def boot(self):
		self.state = State.running
		print('booting the {}'.format(self))

	def kill(self):
		self.state = State.zombie
		print('killing the {}'.format(self))

	def create_process(self,user,filename,permission):
		print('trying to create process {} with user {} with permission {}'.format(filename,user,permission))


	def status(self):
		print('current status is {}'.format(self.state))




class OperatingSystem:

	def __init__(self):
		self.fs = FileServer()
		self.ps = ProcessServer()

	def start(self):

		for i in [self.fs,self.ps]:
			i.boot()

	def kill(self):
		for i in [self.fs,self.ps]:
			i.kill()

	def check(self):
		for i in [self.fs,self.ps]:
			i.status()
# obj = FileServer()
# obj.boot()
# obj.create_file('root','boot.img','write')
# obj.kill()
# obj.status()


# error demo only
# class NewClass(Server):
# 	def __init__(self):
# 		print('in child class')

# 	def show(self):
# 		print('hello')

# obj1 = NewClass()
# obj1.show


obj =OperatingSystem()
obj.start()
obj.check()
obj.kill()
obj.check()
obj.start()
obj.check()