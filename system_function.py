import os, sys

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print basedir

print 'file dir',os.path.dirname(__file__)
# get your file's directory name

print 'file',__file__
#get your file name

print os.path.abspath('.')
#get the currently directory

print sys.stdout.encoding
print os.getcwd()
#get your system coding

#os.startfile('1.mp3')

print 'parent dir', os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if __name__ == "__main__":
    print "Start from here"

