# 流畅的python 
# chapter 1
import collections
import random

def chapter1():
	Card = collections.namedtuple('Card',['rank','suit'])
	card =Card(1,'heart')
	print(card)
	# print(card.rank)

	class FrenchDeck():
		ranks = [str(i) for i in range(2,11)] + list('JQKA')
		suits = 'spades diamonds clubs hearts'.split()

		def __init__(self):
			self._card = [Card(i,j) for i in self.ranks for j in self.suits]

		# 返回长度的特殊方法
		def __len__(self):
			return len(self._card)

		def __getitem__(self,position):
			return self._card[position]



	obj = FrenchDeck()
	print(FrenchDeck.ranks)
	print(FrenchDeck.suits)
	# print(obj._card)
	print('len >>> ',len(obj))
	print('position 20 >>>> ',obj[20])
	for _ in range(10):
		print('random choice >>>>',random.choice(obj))

	print(obj[:3])

def main():
	chapter1()

main()