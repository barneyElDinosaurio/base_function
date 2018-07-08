import pyautogui as pag
import time
screenWidth, screenHeight = pag.size()
print(screenWidth,screenHeight)



def youdao():
	count =0
	time.sleep(3)
	while count < 300:	
		pag.keyDown('down')
		print(count)
		time.sleep(0.03)
		count +=1
	print('done')


def jiaoyi():
	time.sleep(2)
	pag.press('f1')
	time.sleep(2)
	pag.press('f2')
	time.sleep(2)
	# pag.press('tab')
	pag.typewrite('123005')
	pag.press('tab')
	price=129.5
	pag.typewrite(str(price))
	pag.press('tab')
	pag.typewrite('40')
	pag.press('S')
	time.sleep(0.2)
	pag.press('Y')
	time.sleep(0.2)
	pag.press('enter')
	print('done')

def message_win():
	pag.alert("Box")

def photo_compare():
	time.sleep(3)
	print(pag.locateOnScreen('reflash.png'))
# jiaoyi()
# message_win()
# photo_compare()
youdao()