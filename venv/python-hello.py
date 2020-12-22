#print('gi')

import pygame,sys,os
from pygame.locals import *

catx=10
caty=10
screen=0

def myquit():
    pygame.quit()
    sys.exit(0)

def check_inputs(events):
    global catx,caty,screen
    for event in events:
        if event.type==QUIT:
            quit()
        else:
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    myquit()
                elif event.key==K_LEFT:
                    catx-=5
                    print('move rect left')
                elif event.key==K_RIGHT:
                    catx+=5
                    print('move rect right')
                else:
                    print(event.key)
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(catx,50,50,10))
    pygame.display.update()

def main():
    global screen
#red=[255,0,0]

    pygame.init()
    SCREEN_WIDTH=600
    SCREEN_HEIGHT=600

    window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Slither.eat-The Snake Game')
    screen=pygame.display.get_surface()
    pygame.display.update()

    while True:
        check_inputs(pygame.event.get())

main()

#screen.fill(red)
#pygame.display.set_caption("Snake")
#pygame.display.flip()

#count=0




