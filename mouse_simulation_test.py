# -*-coding=utf-8-*-
__author__ = 'Rocky'
import pyautogui as pg
def get_pos():
    cur_x,cur_y=pg.position()
    print cur_x,cur_y

def basic_api():
    '''
    x,y=pg.size()
    print x,y
    '''
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
    pos=[1452 ,321]
    pg.moveTo(pos[0],pos[1])
    pg.doubleClick()
    pg.typewrite(word[0])

    delta_y=50





basic_api()