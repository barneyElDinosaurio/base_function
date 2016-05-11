def yield_test():
    a=1
    for i in range(0,10):
        b=a+i
        yield b

'''
data=yield_test()
print data
for i in range(0,10):
    print data
'''

for i in yield_test():
    print i