# -*-coding=utf-8-*-
__author__ = 'Rocky'
import pyautogui as pg
import pyautogui,time
def get_pos():
    cur_x,cur_y=pg.position()
    print cur_x,cur_y

def basic_api():

    x,y=pg.size()
    print x,y

    '''
    pg.moveTo(300,300,2)
    pg.moveTo(300,400,2)
    pg.moveTo(500,400,2)
    pg.moveTo(500,300,2)
    pg.moveTo(300,300,2)
    #pg.moveTo(300,500,2)
    '''
    #pg.click(100,100)
    word=[u'你好',u'睡了吗']
    pos=[452 ,321]
    pg.moveTo(pos[0],pos[1])
    pg.click()
    pg.typewrite(word[0])

def example():
    screenWidth, screenHeight = pg.size()
    currentMouseX, currentMouseY = pg.position()
    pg.moveTo(500, 550)
    pg.click()
    pg.moveRel(None, 10)  # move mouse 10 pixels down
    pg.doubleClick()
    #pg.moveTo(500, 500, duration=2, tween=pyautogui.tweens.easeInOutQuad)  # use tweening/easing function to move mouse over 2 seconds.
    pg.typewrite('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
    pg.press('esc')
    pg.keyDown('shift')
    pg.press(['left', 'left', 'left', 'left', 'left', 'left'])
    pg.keyUp('shift')
    pg.hotkey('ctrl', 'c')
    delta_y=50



def draw_rect():
    time.sleep(5)
    distance = 200
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0.5)   # move down
        pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0.5)  # move up

def message_test():
    pg.alert('This displays some text with an OK button')
#basic_api()
#example()
#draw_rect()
message_test()