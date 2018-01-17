#-*-coding:utf-8-*-
import os
# 运行环境 python3 （python2的中文编码太蛋疼了）
def rename_file():
    files=os.listdir('.')
    for file in files:
        # print file
        if file.split('.')[-1]=='mp4':
            # print type(file)
            new_name=file.replace(' ','_')
            # print new_name
            # new_name=new_name.encode('unicode-escape')
            # print type(new_name)
            # print file
            # print new_name
            print(file)
            print(type(file))
            print(new_name)
            print(type(new_name))
            cmd='ren \"%s\" \"%s\"' %(file,new_name)
            print(cmd)
            os.system(cmd)
            # os.system('mv {} {}'.format(file,new_name))

def push_file():
    files=os.listdir('.')
    for file in files:
        print(file)
        if file.split('.')[-1]=='mp4':
            cmd='adb push %s /sdcard/rocky' %file
            print(cmd)
            os.system(cmd)

if __name__ == "__main__":
    # print "Start from here"
    os.chdir('D:\\git\\you-get')
    # rename_file()
    push_file()