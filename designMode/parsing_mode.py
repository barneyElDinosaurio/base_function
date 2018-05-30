from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

class Gate:

	def __init__(self):
		self.open =False

	def turn_on(self):
		self.open = True
		print'Gate is opening'

	def __str__(self):
		return 'open' if self.open else 'close'


def main():
	# gate = Gate()
	# print gate
	# gate.turn_on()
	# print gate
	word = Word(alphanums)
	command = Group(OneOrMore(word))
	token = Suppress('->')
	device = Group(OneOrMore(word))
	argument = Group(OneOrMore(word))
	event = command + token + device + Optional(token+argument)

	cmd ='increase -> boiler temperature -> 3 degrees'
	ret,dev,arg = event.parseString(cmd)
	# print ' '.join(ret)
	print ' '.join(ret)
	print dev
	print arg


main()