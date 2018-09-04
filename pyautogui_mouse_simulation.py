# -*-coding=utf-8-*-
__author__ = 'Rocky'
import pyautogui as pag
import pyautogui, time


def basic_api():

    cur_x, cur_y = pag.position()
    print(cur_x, cur_y)

    x, y = pag.size()
    print(x, y)

    '''
    pg.moveTo(300,300,2)
    pg.moveTo(300,400,2)
    pg.moveTo(500,400,2)
    pg.moveTo(500,300,2)
    pg.moveTo(300,300,2)
    #pg.moveTo(300,500,2)
    '''
    # pg.click(100,100)
    # time.sleep(5)
    # word = [u'你好', u'睡了吗']
    # pos = [452, 321]
    # pg.moveTo(pos[0], pos[1])
    # pg.click()
    # pg.typewrite(word[0])

# 滚动有道云笔记
import time
screenWidth, screenHeight = pag.size()
print(screenWidth, screenHeight)

def youdao():
        count = 0
        time.sleep(5)
        while count < 500:
            pag.keyDown('down')
            print(count)
            time.sleep(0.5)
            count += 1
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
    price = 129.5
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

def example():
    screenWidth, screenHeight = pag.size()
    currentMouseX, currentMouseY = pag.position()
    pag.moveTo(500, 550)
    pag.click()
    pag.moveRel(None, 10)  # move mouse 10 pixels down
    pag.doubleClick()
    # pag.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
    pag.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
    pag.press('esc')
    pag.keyDown('shift')
    pag.press(['left', 'left', 'left', 'left', 'left', 'left'])
    pag.keyUp('shift')
    pag.hotkey('ctrl', 'c')
    delta_y = 50


def draw_rect():
    time.sleep(5)
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.5)  # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.5)  # move down
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up


def message_test():
    pag.alert('This displays some text with an OK button')

def web_control():
    x,y=1628, 546
    time.sleep(3)
    n=0
    print(pag.position())
    while n <30:
        for _ in range(15):
            pag.scroll(-500)
            time.sleep(1.1)
        time.sleep(1.5)
        pag.click(x,y)
        time.sleep(3)

# basic_api()
#example()
#draw_rect()
# message_test()
youdao()
# jiaoyi()
# web_control()