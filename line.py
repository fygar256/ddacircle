#!/usr/bin/python3
from pygame.locals import *
import pygame
import sys
import os
import waitkey

def draw_line(screen,p1,p2):
  (x1,y1)=p1
  (x2,y2)=p2
  dx =x2-x1 if x2>x1 else x1-x2
  dy =y2-y1 if y2>y1 else y1-y2
  sx = 1    if x2>x1 else -1
  sy = 1    if y2>y1 else -1
  if ( dx >= dy ):
    e = -dx
    for i in range( dx+1 ):
      set( screen,(x1,y1) )
      x1 += sx
      e += 2*dy
      if ( e>=0 ):
        y1 += sy
        e -= 2*dx
  else:
    e = -dy
    for i in range( dy+1 ):
      set( screen,(x1,y1) )
      y1 += sy
      e+= 2*dx
      if ( e>=0 ):
        x1 +=sx
        e -=2*dy

def set(screen,p):
  screen.set_at(p,(255,255,255))

def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode((200,200))    # 200x200の画面を作成
    pygame.display.set_caption("DDAによる線分描画")    # タイトルを作成
    screen.fill((0,0,0)) # clear screen

    for x in range(0,205,5):
        draw_line(screen,(x,0),(100,100))
        draw_line(screen,(x,200),(100,100))
    for y in range(0,205,5):
        draw_line(screen,(0,y),(100,100))
        draw_line(screen,(200,y),(100,100))

    pygame.display.update()
    key=waitkey.waitkey()
    pygame.quit()
    sys.exit()

if __name__=='__main__':
    main()
