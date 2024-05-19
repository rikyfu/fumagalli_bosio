import pygame
from sys import exit
pygame.init()
from random import randint

screen  = pygame.display.set_mode((600,800))
pygame.display.set_caption('gioco')
clock = pygame.time.Clock()
fps = 60

base = pygame.image.load('immagine/deserto1.png').convert()
base =pygame.transform.scale(base,(600, 100))
deserto = pygame.image.load('immagine/deserto.png').convert()
deserto =pygame.transform.scale(deserto,(600, 800))
vaso= pygame.image.load('immagine/vaso.png').convert_alpha()
vaso =pygame.transform.scale(vaso,(150, 150))
while True:
    #programma
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()

   
    screen.blit(deserto,(0,0))
    screen.blit(base,(0,700))
    screen.blit(vaso,(225,570))
    

    

    pygame.display.update() 
    clock.tick(fps) 