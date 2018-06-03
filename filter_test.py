# python2 diff python3
s = ['Hello', 'World', 'This', 'is', 'My', 'World', 'Issris', 'issue']
result = filter(lambda x:x.lower().startswith('i') , s)
print(next(result))
print(type(result))
print(result)
print(list(result))
