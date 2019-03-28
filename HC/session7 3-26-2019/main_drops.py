

# size(640, 360);
import pygame
import purple_rain

# I copied the width and height from Daniel Shiffman's video
#The underscores are probably not nessasary
width = 640
height = 360

drops = []

# # loop for initiating drops
# for i in range(10):
#     drops.append(purple_rain.Drop())


pygame.init()

screen = pygame.display.set_mode((width,height))

# loop for initiating drops
for i in range(500):
    drops.append(purple_rain.Drop(screen))

game = True
clock = pygame.time.Clock()


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    #purple color
    purple_color = (151, 88, 239)

    screen.fill((0,0,0))
    for drop in drops:
        drop.fall()
        drop.show()

    #pygame.draw.line(screen,purple_color,[width/2,height/2],[width/2,(height/2+8)],1)
    pygame.display.flip()
    clock.tick(60)
