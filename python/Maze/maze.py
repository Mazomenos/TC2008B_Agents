"""
Graficación utilizando Pygame
Laberinto
TC2008B
Gustavo Betancourt Mazomenos
A01252832
08/08/23
"""


# Importacion de librerias
import pygame, sys 
from pygame.locals import *

# Variables Universales
WIDTH = 600
HEIGHT = 600
SPEED = 10

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

# Coordenadas
x1 = 150
y1 = 150

l1 = [(50,50),(550,50),(550,500),(250,500),(250,450),(250,500),(200,500)]
f1_1 = [(350,50),(350,300),(500,300),(500,450),(500,300),(450,300),(450,450),(400,450),(400,400),(350,400),(350,350),(400,350)]
f1_2 = [(450,50),(450,100),(500,100),(500,250),(400,250),(500,250),(500,150),(450,150),(450,200),(400,200),(400,100)]
f1_3 = [(300,500),(300,400),(150,400),(200,400),(200,450)]

l2 = [(550,550),(50,550),(50,100),(300,100),(300,250),(150,250),(150,150),(250,150),(250,200),(200,200)]
f2_1 = [(150,550),(150,450),(150,500),(100,500),(100,400)]
f2_2 = [(100,100),(100,350),(300,350),(300,300),(150,300)]


# Tamaños

# Se inicializa la libreria de pygame
pygame.init()

# Se declara la ventana con sus dimensiones
screen = pygame.display.set_mode((WIDTH,HEIGHT))

char_img = pygame.image.load("hello.png").convert_alpha()
char_rect = char_img.get_rect()
char_rect.x = 10
char_rect.y = 55

# Atributo adicional para personalizar la ventana
pygame.display.set_caption('Laberinto')


# Loop donde se ejecuta la ventana
while True:

    # Loop donde se espera algun evento
    for event in pygame.event.get():
        # Se llena el fondo con un color
        screen.fill(WHITE)

        # Declaracion de objetos pintados
        #c1 = pygame.draw.rect(screen,WHITE, (x1,y1,300,300))
        #c2 = pygame.draw.rect(screen,MAGENTA, (200,200,200,200))

        lines1 = pygame.draw.lines(screen, BLACK, False, l1,2)
        fork1_1 = pygame.draw.lines(screen, BLACK, False, f1_1,2)
        fork1_2 = pygame.draw.lines(screen, BLACK, False, f1_2,2)
        fork1_2 = pygame.draw.lines(screen, BLACK, False, f1_3,2)

        lines2 = pygame.draw.lines(screen, BLACK, False, l2,2)
        fork2_1 = pygame.draw.lines(screen, BLACK, False, f2_1,2)
        fork2_2 = pygame.draw.lines(screen, BLACK, False, f2_2,2)

        screen.blit(char_img, char_rect)
        

        # Evento que fianliza codigo al cerrar la ventana
        if event.type == QUIT:
            sys.exit()

        # Eventos al tocar teclas del teclado
       


        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and char_rect.top > 0:
           char_rect.y -= SPEED 
        if keys[pygame.K_s] and char_rect.bottom < HEIGHT-20:
           char_rect.y += SPEED
        if keys[pygame.K_a] and char_rect.left > 0:
           char_rect.x -= SPEED
        if keys[pygame.K_d] and char_rect.right < WIDTH-20:
           char_rect.x += SPEED

    # Actualiza la ventana mientras se este ejecutando
    pygame.display.update()