import pygame
from pygame.locals import *

pygame.init()

win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_BACKSPACE):
            run = False

    win.fill((0, 0, 0))

    pygame.draw.circle(win, (255, 0, 0), (300, 200), 50)

    pygame.display.flip()

pygame.quit()