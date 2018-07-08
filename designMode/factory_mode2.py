
MINI14='apple mac 14 mini'
class Computer:
	def __init__(self,serialNo):
		self.serialNo=serialNo
		self.memory=None
		self.hd=None
		self.gpu=None

	def __str__(self):
		info = ('Model: {};'.format(MINI14),
				'Memory: {};'.format(self.memory),
				'GPU: {};'.format(self.gpu))
		return ''.join(info)

class ComputerBuilder:

	def __init__(self):
		self.computer = Computer('ABCDEF')

	def configure(self,mem,hd,gpu):
		self.computer.memory = mem
		self.computer.hd = hd
		self.computer.gpu = gpu



class Engineer:
	def __init__(self):
		self.builder = None

	def build(self):
		self.builder=ComputerBuilder()
		self.builder.configure(8,500,'Intel HD 5000')

	@property
	def computer(self):
		return self.builder.computer


def main():
	pcfactory = Engineer()
	pcfactory.build()
	print(pcfactory.computer)



main()