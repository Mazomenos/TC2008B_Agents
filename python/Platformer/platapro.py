#Librerias
import sys
import random
import pygame as pg

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

#Declarar Variables

WIDTH, HEIGHT = 720, 400
SPEED, FPS = 5, 60

# Atributo adicional para personalizar la ventana
pg.display.set_caption('Platformer')

pg.init()
display = pg.display.set_mode((WIDTH, HEIGHT))



while True:

    for event in pg.event.get():
        #Quit button
        if event.type == pg.QUIT:
            sys.exit()




    #Update Frames
    pg.display.update()