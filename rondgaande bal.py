import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

win = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


background = pygame.image.load("wallpaper.png")
background = pygame.transform.scale(background, (800, 600))


collision_sound = pygame.mixer.Sound("half-life-crowbar.mp3")

x = 300
y = 200
radius = 50

speed_x = 5
speed_y = 4

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_BACKSPACE):
            run = False

        if event.type == KEYDOWN:
            if event.key == K_UP:
                speed_x += 1
                speed_y += 1
            elif event.key == K_DOWN:
                speed_x -= 1
                speed_y -= 1


    x += speed_x
    y += speed_y


    if x + radius > 800 or x - radius < 0:
        speed_x *= -1
        collision_sound.play()

    if y + radius > 600 or y - radius < 0:
        speed_y *= -1
        collision_sound.play()


    speed = abs(speed_x) + abs(speed_y)
    if speed > 10:
        color = (255, 0, 0)
    else:
        color = (0, 0, 255)


    win.blit(background, (0, 0))
    pygame.draw.circle(win, color, (x, y), radius)

    pygame.display.flip()

pygame.quit()