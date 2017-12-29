import struct,os
data_path=os.path.join(os.getcwd(),'data')
os.chdir(data_path)
mask='5s11s1s'
with open('dingkuan_data.txt','r') as f:
	for line in f:
		# print line
		fields=struct.Struct(mask).unpack_from(line)
		print fields
		print '*'*10
