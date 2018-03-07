# -*-coding=utf-8-*-
import codecs

__author__ = 'Rocky'
import os, re


def func():
	cwd = os.getcwd()
	print cwd
	cwd1 = os.path.dirname(__file__)
	print cwd1
	# p = re.compile('\.txt')
	# print cwd
	# for dirpath, dirname, filename in os.walk(cwd):
	#     # print dirpath,dirname,filename
	#     #print dirpath
	#     print dirname
	#     print type(filename)
	#     if filename is not None:
	#         for i in filename:
	#             #if filename is not None:


#
#             if p.search(i):
#                 os.remove(os.path.join(dirpath, i))


def testcase1():
	i = "memory"
	sub_folder = os.path.join(os.getcwd(), i)
	print sub_folder


def testcase2():
	# read/readline/readlines
	f1 = open('data.cfg', 'r')
	r1 = f1.read()
	print 'type of r1 ', type(r1)
	print 'content of r1 ', r1
	f1.close()

	f2 = open('data.cfg', 'r')
	r2 = f2.readlines()

	print 'type of r2 ', type(r2)
	print 'content of r2 ', r2
	f2.close()

	f3 = open('data.cfg', 'r')
	r3 = f3.readline()

	print 'type of r3 ', type(r3)
	print 'content of r3 ', r3
	r3 = f3.readline()

	print 'type of r3 ', type(r3)
	print 'content of r3 ', r3

	r3 = f3.readline()

	print 'type of r3 ', type(r3)
	print 'content of r3 ', r3

	f3.close()


def testcase4():
	fp = codecs.open('data/house_10.cfg', 'r', encoding='utf-8')
	data = fp.readlines()
	# print data[:5]
	print len(data)
	data = map(lambda x: x.split()[3:6], data)

	for i in range(5):
		print data[i][0]
		print data[i][2]
		# print data[i][2]

	print len(data)


# 写入缓冲
def testcase5():
	f = open('data/buffer.txt', 'w', buffering=1)
	f.write("Hello world")


def testcase6():
	file = os.listdir('.')
	for i in file:
		print i


def main():
	# testcase6()
	func()


if __name__ == '__main__':
	main()
