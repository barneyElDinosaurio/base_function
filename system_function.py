#-*-coding:utf-8-*-
import os, sys

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(basedir)

print('file dir',os.path.dirname(__file__))
# get your file's directory name

print('file',__file__)
#get your file name

print(os.path.abspath('.'))
#get the currently directory

print(sys.stdout.encoding)
print(os.getcwd())
#get your system coding

#os.startfile('1.mp3')

print('parent dir', os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

def rename_file():
    files=os.listdir('.')
    for file in files:
        # print(file)
        if file.split('.')[-1]=='xxx':
            # print(type(file))
            current= file.decode('gb2312')
            new_name=current.replace(u'儿歌多多 ','')
            # print(new_name)
            new_name=new_name.encode('unicode-escape').decode('string_escape')
            print(type(new_name))
            print(file)
            print(new_name)
            os.system('mv \'{}\' \'{}\''.format(current,new_name))
if __name__ == "__main__":
    print("Start from here")
    rename_file()
