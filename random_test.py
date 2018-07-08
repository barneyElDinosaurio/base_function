__author__ = 'rocky'
import random
# list=[1,2,3,4,5]
#print(list[2])

list = []
'''
for i in range(536870911):
    list.append(random.random())

'''
'''
for _ in xrange(100):
    print(random.random())
#print(len(list))
'''

def round_case():
    raw_input("input barcode")
    a=int(round(random.random()*1000))
    print(a)

def random_case():
    print(random.randint(2,10)*random.random())

def random_select():
    a=['R','O','C','K','Y']
    x=random.choice(a)
    print(x)
#round_case()
#random_case()
random_select()
