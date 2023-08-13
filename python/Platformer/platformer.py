"""
Act
Platformer
TC2008B
Gustavo Betancourt Mazomenos
A01252832
11/08/23
"""

import sys
import random
import pygame as pg

WIDTH, HEIGHT = 720, 400
SPEED, FPS = 5, 60

# Colores (constantes)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Atributo adicional para personalizar la ventana
pg.display.set_caption('Platformer')

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
background = pg.image.load("grass.png").convert_alpha()
dino_image = pg.image.load("dino.png").convert_alpha()
dino_rect = dino_image.get_rect()
star_image = pg.image.load("star.png").convert_alpha()
star_rect = star_image.get_rect()
star_rect.center = (WIDTH//2, HEIGHT//2)
clock = pg.time.Clock()




while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

    clock.tick(FPS)

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and dino_rect.left > 0:
        dino_rect.x -= SPEED
    if keys[pg.K_RIGHT] and dino_rect.right < WIDTH:
        dino_rect.x += SPEED


    if keys[pg.K_UP] and dino_rect.top > 0:
        dino_rect.y -= SPEED
    if keys[pg.K_DOWN] and dino_rect.bottom < HEIGHT:
        dino_rect.y += SPEED

    if dino_rect.colliderect(star_rect):
        star_rect.x = random.randint(50, WIDTH - 50)
        star_rect.y = random.randint(50, HEIGHT - 50)
        print("COLISION")

    display.blit(background, (0, 0))
    display.blit(dino_image, dino_rect)
    display.blit(star_image, star_rect)
    c1 = pg.draw.rect(display,RED, (200,200,100,100))

    SPEED = 5

    if dino_rect.colliderect(c1):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and dino_rect.left > 0:
            dino_rect.x += SPEED
        if keys[pg.K_RIGHT] and dino_rect.right < WIDTH:
            dino_rect.x -= SPEED
        if keys[pg.K_UP] and dino_rect.top > 0:
            dino_rect.y += SPEED
        if keys[pg.K_DOWN] and dino_rect.bottom < HEIGHT:
            dino_rect.y -= SPEED
        
        print("COLISION")   

    pg.display.update()
    