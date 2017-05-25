#-*-coding=utf-8-*-
__author__ = 'xda'
import subprocess,os,time

os.system('adb reboot forced-recovery')
time.sleep(10)
cmd='export BOARD=p2894-0050-a04;./flash.sh -f'
p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
output,error=p.communicate()
