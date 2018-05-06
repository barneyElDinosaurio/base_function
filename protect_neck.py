import pyautogui as pag
import datetime
def ready_rest():
	f= open('record.txt','a')
	ret = pag.prompt("Rest! Protect your neck !")
	if ret =='rest':
		f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		f.write('\t')
		f.write('Rest')
		f.write('\n')
	else:
		f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		f.write('\t')
		f.write('Failed to rest')
		f.write('\n')
	f.close()

ready_rest()