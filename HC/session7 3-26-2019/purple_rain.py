
import pygame
import random
from numpy import interp
import constants

width = constants.width
height = constants.height

x_range_start = constants.x_range_start
x_range_end = constants.x_range_end
#note: I could also have x range shift dynamically and put it in the __init__ function instead

pygame.init()

class Drop:
    def __init__(self,screen):
        # width is the value of the width of the screen

        self.x = random.randint(x_range_start,x_range_end)
        #self.x = random.randint(0,width)
        self.y = random.randint(-500,-50)
        self.z = random.randint(0,20)
        self.drop_len = interp(self.z,[0,20],[10,20])
        self.yspeed = interp(self.z,[0,20],[1,20])
        self.screen = screen

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
        purple_color = constants.purple_color
        pygame.draw.line(self.screen,purple_color,[self.x,self.y],[self.x,self.y + self.drop_len],int(thick))

        # look up how to make a line in pygame



#
