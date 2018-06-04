# coding: utf-8
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                   dest="quiet", 
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
print options
print args
print type(options)
print options.filename

print '\n'*5

def dict_args(*args, **kwargs):

	print args
	print kwargs
	print kwargs.get('b')

dict_args(a='1',b='admin')