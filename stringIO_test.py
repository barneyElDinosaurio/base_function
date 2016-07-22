__author__ = 'rocchen'
import StringIO
str_temp=StringIO.StringIO("abcdEFGHIHK")
#str_temp.write("Rocky")
str_temp.seek(0)
print str_temp.read()

str_temp.seek(0)
str_temp.write("rocky")
str_temp.seek(0)
print str_temp.read()


s = StringIO.StringIO()
s.write("aaaa")
lines = ['xxxxx', 'bbbbbbb']
s.writelines(lines)
s.seek(0)
print s.read()
print s.getvalue()
s.write(" ttttttttt ")
s.seek(0)
print s.readlines()
print s.len


i=StringIO.StringIO("123456789")
i.seek(9)
i.write("abcd\r\n")
i.seek(0)
print i.read()