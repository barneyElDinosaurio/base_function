# -*-coding=utf-8-*-
class X:
    pass


# python2 非法
# X.__class__

class Rectangle:
    def area(self):
        # 居然可以不用初始化， 类实例化后可以直接赋值
        # 不好的习惯， 避免
        return self.width * self.height


rec = Rectangle()
rec.width, rec.height = 10, 20
print rec.area()


class Suit():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get(self):
        return self.name, self.symbol


Club, Diamond, Heart, Spade = Suit('Culb', '梅花'), Suit('Diamond', '钻石'), Suit('Heart', '红心'), Suit('Spade', '葵扇')


class Card():
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10

cards = [AceCard('A',Spade),NumberCard('2',Heart)]
for i in cards:
    print i
rank=10
class_ = {1:AceCard,11:FaceCard,12:FaceCard,13:FaceCard}.get(rank,NumberCard)

print class_