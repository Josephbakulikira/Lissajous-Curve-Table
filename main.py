import pygame
import os
import math
from Curve import Curve
import colorsys
import numpy as np
os.environ["SDL_VIDEO_CENTERED"]='1'

width, height = 1920, 1080
size = (width, height )
h = 0
def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

pygame.init()
pygame.display.set_caption("Lissajous Curves")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

white, black, gray = (245, 245, 245), (15, 15, 15), (150, 150, 150)
angle = 0
w = 100
columns = width//w-1
rows = height// w-1
speed = 0.01
radius = int((w//2) - 0.1*w)
curves = [[i for i in range(columns)] for j in range(rows)]

for x in range(rows):
    for y in range(columns):
        curves[x][y] = Curve(hsv_to_rgb(h, 1, 1))
        h+= 0.001
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

      
    for i in range(columns):
        a = w+10 + i * w + w//2
        b = w//2 + 15
        pygame.draw.circle(screen, white, (a, b), int(radius), 1)

        x = radius * math.cos(angle*(i+1) - math.pi/2)
        y = radius * math.sin(angle*(i+1) - math.pi/2)
        pygame.draw.line(screen, gray, (int(a+x), 0), (int(a+x), height), 1)
        pygame.draw.circle(screen, white, (int(a+x), int(b+y)), 8)
        for j in range(rows):
            curves[j][i].set_point_x(a+x)

    for j in range(rows):
        a = w//2 + 15
        b = w+10 + j * w + w//2
        pygame.draw.circle(screen, white, (a, b), radius, 1)

        x = radius * math.cos(angle*(j+1) - math.pi/2)
        y = radius * math.sin(angle*(j+1) - math.pi/2)
        pygame.draw.line(screen, gray, (0, int(b+y)), (width, int(b+y)), 1)
        pygame.draw.circle(screen, white, (int(a+x), int(b+y)), 8)
        for i in range(columns):
            curves[j][i].set_point_y(b+y)
    
    
    for x in range(rows):
        for y in range(columns):
            curves[x][y].update_points()
            curves[x][y].draw(screen)

    angle-= speed
    if angle < - 2 * math.pi:
        for x in range(rows):
            for y in range(columns):
                curves[x][y].points = []
        angle = 0

    pygame.display.update()
#pygame.image.save(screen, "screenshot.jpg")
pygame.quit()
