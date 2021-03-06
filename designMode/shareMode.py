import random
from enum import Enum
TreeType =Enum('TreeType','apple_tree cherry_tree peach_tree')

class Tree(object):
	pool =dict()
	def __new__(cls,tree_type):
		obj = cls.pool.get(tree_type,None)
		if not obj:
			obj = object.__new__(cls)
			cls.pool[tree_type]=obj
			obj.tree_type=tree_type
		return obj

	def render(self,age,x,y):
		print('render a tree of type {} and age at ({},{})'.format(self.tree_type,age,x,y))


# for i in range(100):
# 	t = Tree(TreeType.apple_tree)
# 	t.render(i,12,13)

t1 = Tree(TreeType.apple_tree)
t2 = Tree(TreeType.cherry_tree)
t3 = Tree(TreeType.apple_tree)
print(id(t1),id(t2),id(t3))
