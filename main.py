import pygame
from sys import exit
pygame.init()
from random import randint
from pygame.locals import *
from vaso import Vaso

screen  = pygame.display.set_mode((600,800))
pygame.display.set_caption('il vaso di Pandora')
clock = pygame.time.Clock()
fps = 60
vel_vaso = 5

base = pygame.image.load('immagine/deserto1.png').convert()
base =pygame.transform.scale(base,(600, 100))
deserto = pygame.image.load('immagine/deserto.png').convert()
deserto =pygame.transform.scale(deserto,(600, 800))
# vaso = pygame.image.load('immagine/vaso.png').convert_alpha()
# vaso =pygame.transform.scale(vaso,(150, 150))
vaso = Vaso(screen,[225,570],[10,10])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()

    keys = pygame.key.get_pressed()
    # tasti per movimento del vaso
    if keys[K_RIGHT]:
       vaso.moveright(vel_vaso)
    if keys[K_LEFT]:
        vaso.moveleft(vel_vaso)
    
    # DISEGNO SFONDO
    screen.blit(deserto,(0,0))
    screen.blit(base,(0,700))
    # disegno vaso
    vaso.draw()
    # screen.blit(vaso,(225,570))
    

    

    pygame.display.update() 
    clock.tick(fps) 