# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
from functools import partial
import datetime
def save_file(content,file_name):
    try:
        f=open(file_name,'a')
        f.write(content)
        f.write('\n')
        f.close()
    except Exception as e:
        print e
        return

def running_log():
    now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content=now+"  execute the script"
    filename='logfile.txt'
    to_file=partial(save_file,file_name=filename)
    to_file(content)


def main():
    running_log()

if __name__=='__main__':
    main()
