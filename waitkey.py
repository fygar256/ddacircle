from pygame.locals import *
import pygame

def waitkey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if event.type == KEYDOWN:  # キーを押したとき
                k=pygame.key.name(event.key)
                return(k)


