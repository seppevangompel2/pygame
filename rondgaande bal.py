import pygame
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 50
y = 200
speed = 5

run = True
while run:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_BACKSPACE):
            run = False


    x += speed
    if x + 50 > 800:
        speed = -speed
    if x - 50 < 0:
        speed = -speed

    win.fill((0, 0, 0))


    pygame.draw.circle(win, (255, 0, 0), (x, y), 50)

    pygame.display.flip()

pygame.quit()