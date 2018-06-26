fp = open('demo','r')
content = fp.readlines()
result =[]
for line in content:
    keys= line.strip().split('=')
    # print(keys)
    if keys[0]!='':
        result.append('{}=item[\'{}\'],\n'.format(keys[0].strip(),keys[0].strip()))
# print(result)
print(''.join(result))

