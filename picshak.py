#_*_coding:utf8_*_

import pygame,sys #导入pygame
from pygame.locals import *
pygame.init() #初始化 display,image,mix等模块
screen=pygame.display.set_mode((860,660))#设置窗体大小或列表
pygame.display.set_caption("hello world")#设置标题
cc=[(255,0,0),(26,10,0),(160,255,20),(60,45,200),(20,178,255),
(76,100,0),(10,100,20),(160,45,200),(20,578,30)]
pos_x = 0
pos_y = 0
vel_x = 0.8
vel_y = 0.4
color= 0,0,0
i=0
#-------------插入音乐----------------
pygame.mixer.music.load("abc.mp3")
pygame.mixer.music.play(-1)
#-------------插入文字----------------
fontbj=pygame.font.SysFont("stkaiti",36,italic=True)
text=fontbj.render(u"hello world",True,(255,255,0),(128,128,128))
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    screen.fill((0,0,200))
    pos_x += vel_x
    pos_y += vel_y
    if pos_x > 760 or pos_x < 0:
        vel_x = -vel_x
        i+=1
        if i>=8:
            i=0
        color= cc[i]   
        #---音效---
        yx=pygame.mixer.Sound("blap.wav")
        yx.play()
    if pos_y > 560 or pos_y < 0:
        vel_y = -vel_y
        i+=1
        if i>=8:
            i=0
        color= cc[i] 
        #---音效---
        yx=pygame.mixer.Sound("blap.wav")
        yx.play()      
    width = 0
    pos = pos_x,pos_y,100,100
    pygame.draw.rect(screen, color, pos, width)   
    screen.blit(text,(360,380))
    pygame.display.update()
#结束
pygame.quit()
