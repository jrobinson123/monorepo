
import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    #if pressed[pygame.K_UP]: y -= 3
    # is it good to use elif statements in this case?
    if pressed[pygame.K_UP]:
        y -= 3
    elif pressed[pygame.K_DOWN]:
        y += 3
    elif pressed[pygame.K_LEFT]:
        x -= 3
    elif pressed[pygame.K_RIGHT]:
        x += 3
    # is the color rgb 0-255?
    #note: it's pretty cool to comment out the bellow line?
    screen.fill((0,0,0))
    if is_blue:
        color = (0,100,200)
    else:
        color = (200,255,0)
    # why do I have to use multiple dots(dots as in .)
    pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))

    pygame.display.flip()
    clock.tick(60)
