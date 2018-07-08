#-*-coding=utf-8-*-
def permutation(up,down):
	sum=1
	for i in range(down,down-up,-1):

		sum=sum*i

	return sum

# print(permutation(5,6))

def combination(up,down):
	numerator=permutation(up,down)
	denominator=permutation(up,up)
	return numerator/denominator

denominator=combination(1,16)*combination(6,33)
first=1.0/denominator
second=1.0*combination(1,15)/denominator
third=1.0*combination(1,27)/denominator
forth=1.0*(combination(1,15)*combination(1,27)+combination(1,15)*combination(2,27))/denominator
print( u'一等奖的概率{}'.format(first))
print( u'二等奖的概率{}'.format(second))
print( u'三等奖的概率{}'.format(third))
print( u'四等奖的概率{}'.format(forth))

