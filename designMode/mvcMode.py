quotes= ['A man is not complete until he is married. Then he is finished.',
'As I said before, I never repeat myself.',
'Behind a successful man is an exhausted woman.',
'Black holes really suck...', 'Facts are stubborn things.']
class QuoteView(object):
	def show(self,quote):
		print('And the quote is {}'.format(quote))

	def error(self,msg):
		print('Error: {}'.format(msg))

	def select_quote(self):
		return input('Which quote number you like to see ?\n')

class QuoteModel(object):
	def get_quote(self,n):
		try:
			ret = quotes[n]
		except:
			ret = 'Not found'
		print(ret)
		return ret


class QuoteController(object):
	def __init__(self):
		self.view = QuoteView()
		self.model = QuoteModel()

	def run(self):
		n = self.view.select_quote()
		# print(type(n))
		ret =self.model.get_quote(n)
		self.view.show(ret)

def main():
	obj = QuoteController()
	while 1:
		obj.run()

main()