MINI14 = ' 1.4Ghz mac Mini'
class AppleFactory:
	class MacMini14:
		def __init__(self):
			self.memory = 4
			self.hd = 500
			self.gpu='Intel HD Graphic 5000'

		def __str__(self):
			info = ('Model: {};'.format(MINI14),
				'Memory: {};'.format(self.memory),
				'GPU: {};'.format(self.gpu))
			return ''.join(info)

	def build(self):
		return self.MacMini14()


def main():
	appfac = AppleFactory()
	mac = appfac.build()

	print(mac)



main()