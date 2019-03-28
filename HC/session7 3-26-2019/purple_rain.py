
import pygame
import random
from numpy import interp

width = 640
height = 360

pygame.init()

class Drop:
    def __init__(self,screen_):
        # width is the value of the width of the screen
        self.x = random.randint(0,width)
        self.y = random.randint(-500,-50)
        self.z = random.randint(0,20)
        self.drop_len = interp(self.z,[0,20],[10,20])
        self.yspeed = interp(self.z,[0,20],[1,20])
        self.screen_ = screen_

    def fall(self):
        self.y += self.yspeed
        grav = interp(self.z,[0,20],[0,0.2])
        self.yspeed += grav

        #height needs to be defined along with width
        if (self.y > height):
            self.y = random.randint(-200,-100)
            self.yspeed = interp(self.z,[0,20],[4,10])

    def show(self):
        thick = interp(self.z,[0,20],[1,3])
        # strokeWeight()
        # stroke(138,43,226)
        # line(x,y,x,y+dro_len)
        purple_color = (151, 88, 239)
        screen = pygame.display.set_mode((width,height)
        pygame.draw.line(self.screen_,purple_color,[self.x,self.y],[self.x,self.y + self.drop_len],1)

        # look up how to make a line in pygame



#
