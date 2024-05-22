import pygame
from sys import exit
pygame.init()
from random import randint
from pygame.locals import *
from vaso import Vaso
from pozione import Pozione
from moneta import Moneta

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('il vaso di Pandora')
clock = pygame.time.Clock()
fps = 60
vel_vaso = 7

base = pygame.image.load('immagine/deserto1.png').convert()
base =pygame.transform.scale(base,(600, 100))
deserto = pygame.image.load('immagine/deserto.png').convert()
deserto =pygame.transform.scale(deserto,(600, 800))
# pozione = pygame.image.load('immagine/pozione.png').convert_alpha()
# pozione =pygame.transform.scale(pozione,(70, 70))
# moneta = pygame.image.load('immagine/moneta.png').convert_alpha()
# moneta =pygame.transform.scale(moneta,(65, 65))
# vaso = pygame.image.load('immagine/vaso.png').convert_alpha()
# vaso =pygame.transform.scale(vaso,(150, 150))

vaso = Vaso(screen,[225,585],[175,175])
moneta = Moneta([65,65])
pozione = Pozione([70,70])
piu_moneta = pygame.USEREVENT + 1
pygame.time.set_timer(piu_moneta,1200)
piu_pozione = pygame.USEREVENT + 1
pygame.time.set_timer(piu_pozione,1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
    
    screen.blit(deserto,(0,0))

    keys = pygame.key.get_pressed()
    # tasti per movimento del vaso
    if keys[K_RIGHT]:
       vaso.moveright(vel_vaso)
    if keys[K_LEFT]:
        vaso.moveleft(vel_vaso)
   
    
    # # if event.type == piu_pozione:
    moneta.update(screen)
    moneta.draw(screen)

    # if event.type == piu_pozione:
    pozione.update(screen)
    pozione.draw(screen)

    

    screen.blit(base,(0,740))
    # disegno vaso
    vaso.draw()
 

   # screen.blit(vaso,(225,570))

    pygame.display.flip() 
    clock.tick(fps) 