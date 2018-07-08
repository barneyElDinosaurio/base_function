# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import subprocess,os
def git_sync():
    current=os.getcwd()
    fetch='git fetch origin'
    status='git status'
    for (dirname,dirs,filename) in os.walk('.'):
        #print(dirname)
        #print(dirs)
        #print(filename)
        for dir in dirs:
            path=os.path.join(current,dir)
            os.chdir(path)
            #print(os.getcwd())
            try:

                print(path)
                #print(os.listdir('.'))
                os.system('git status')
                p=subprocess.Popen(fetch,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                p.communicate()
                p.wait()
                print(p.stdout.read())
                p=subprocess.Popen(status,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
                p.communicate()
                p.wait()
                print(p.stderr.read())
            except Exception as e:
                print(e)
        break

    #print(os.listdir(current))


git_sync()