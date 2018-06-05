#-*coding:utf-8-*-
from warnings import warn
# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类


class Foo(type):
	def __init__(cls, name, bases, attrs):
		super(Foo,cls).__init__(name, bases, attrs)
		print 'define on Foo, meta class'
		if '__str__' not in attrs:
			warn('No __str__ method')

print 'After foo before bar'
class Bar(object):
	__metaclass__ = Foo

	def __init__(self):
		print 'define on Bar'

	def __str__(self):
		return 'Bar is my home'


# L = MyList()
# L.add(2)
# print L

print 'main'
b = Bar()
print 'end'

print b
