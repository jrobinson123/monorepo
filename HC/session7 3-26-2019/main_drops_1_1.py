

import pygame
import purple_rain
import constants


width = constants.width
height = constants.height


drops = []

pygame.init()

screen = pygame.display.set_mode((width,height))

#the variable drops_created represent the amount of drops that are going to be created
drops_created = int((width/640) * 500)
print(drops_created)


# loop for initiating drops
for i in range(drops_created):
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
