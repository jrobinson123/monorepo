

# size(640, 360);
import pygame
import purple_rain
import constants

# I copied the width and height from Daniel Shiffman's video
#The underscores are probably not nessasary
width = constants.width
height = constants.height

drops = []

# # loop for initiating drops
# for i in range(10):
#     drops.append(purple_rain.Drop())


pygame.init()

screen = pygame.display.set_mode((width,height))


# loop for initiating drops
for i in range(500):
    drops.append(purple_rain.Drop(screen))


clock = pygame.time.Clock()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    screen.fill((0,0,0))
    for drop in drops:
        drop.fall()
        drop.show()

    pygame.display.flip()
    clock.tick(60)
