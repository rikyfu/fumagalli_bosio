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
gameover = pygame.image.load('immagine/gameover.png').convert_alpha()
vaso = Vaso(screen,[225,585],[175,175])

oggetti = []
timer = 0

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

    # creazione oggetti
    if timer == 0:
        cosa = randint(0,6)
        if cosa == 0 or cosa == 3 or cosa == 5:
             oggetti.append(Moneta([65,65]))
            
        else:
             oggetti.append(Pozione([70,70],vaso))
             

            
        
        min = 10* fps
        max = 15 * fps
        timer = randint(min, max)
    timer -= 1

    # disegno gli oggetti
    for oggetto in oggetti:
        oggetto.update(screen)
        oggetto.draw(screen)
       
       
    
    screen.blit(base,(0,740))
    # disegno vaso

    vaso.draw()
    
   

  

   # screen.blit(vaso,(225,570))

    pygame.display.flip() 
    clock.tick(fps) 