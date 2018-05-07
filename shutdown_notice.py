import pyautogui as pag
import datetime
def ready_rest():
	f= open('shutdownrecord.txt','a')
	ret = pag.prompt("System going to shutdown!")
	if ret =='confirm':
		f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		f.write('\t')
		f.write('Shutdown')
		f.write('\n')
	else:
		f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		f.write('\t')
		f.write('Failed to shutdown')
		f.write('\n')
	f.close()

ready_rest()