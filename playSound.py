#play sound in python
import os,subprocess
media_path="/Users/rocky/Data/shutter.wav"
cmd1 = "mplayer %s" %media_path
cmd='uname -a'
print cmd
result = os.popen(cmd1)
print result.read()
status=os.system(cmd1)
print status

myresult = subprocess.Popen(['mplayer',media_path],stdout=subprocess.PIPE)
myresult.wait()

print myresult.stdout.read()

print os.times()
print os.uname()