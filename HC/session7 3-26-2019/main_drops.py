

# size(640, 360);
import pygame
import purple_rain

# I copied the width and height from Daniel Shiffman's video
#The underscores are probably not nessasary
width_ = 640
height_ = 360

drops = []

# # loop for initiating drops
# for i in range(10):
#     drops.append(purple_rain.Drop())


pygame.init()

screen = pygame.display.set_mode((width_,height_))

# loop for initiating drops
for i in range(10):
    drops.append(purple_rain.Drop(screen))

game = True
clock = pygame.time.Clock()


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #purple color
    purple_color = (151, 88, 239)

    for drop in drops:
        drop.fall()
        drop.show()

    pygame.draw.line(screen,purple_color,[width_/2,height_/2],[width_/2,(height_/2+8)],1)
    pygame.display.flip()
    clock.tick(60)
