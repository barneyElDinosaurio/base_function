#-*-coding=utf-8-*-
import os,sys,subprocess
import re

# 输入进程名字，杀死该进程
def get_process(name):
    cmd='ps -aux | grep {}'.format(name)
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    target =  p.stdout.read()
    pids = re.findall('xda\s+(.*?)\s+',target)
    if not pids:
        return

    for pid in pids:
        kill_cmd ='kill -9 {}'.format(pid)
        p = subprocess.Popen(kill_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        p.communicate()
        p.wait()

def old_function():
    f=open('kill_id.txt')
    data = f.readlines()
    #print data
    for i in data:
        kid= i.split()[1]
        os.system('kill %s' %kid)

def main():
    get_process('plot_test.py')


if __name__ == '__main__':
    main()