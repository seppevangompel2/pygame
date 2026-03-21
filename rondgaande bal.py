import pygame
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 300
y = 200
radius = 50

speed_x = 5
speed_y = 4

run = True
while run:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_BACKSPACE):
            run = False

    x += speed_x
    y += speed_y

    if x + radius > 800 or x - radius < 0:
        speed_x *= -1

    if y + radius > 600 or y - radius < 0:
        speed_y *= -1

    win.fill((0, 0, 0))

    pygame.draw.circle(win, (255, 0, 0), (x, y), radius)

    pygame.display.flip()

pygame.quit()