import pygame
from sys import exit
pygame.init()
from random import randint
from pygame.locals import *
from vaso import Vaso
from moneta2 import Moneta2
from moneta import Moneta
from pozione import Pozione
from bottone_tavolo import Bottone
from bottone_tavolo import Tavolo

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
# pozione = pygame.image.load('immagine/pozione.png').convert_alpha()
# pozione =  pygame.transform.scale(pozione,(75, 75))
# pos_y = -randint(20,40)
# pos_x = randint(0,600)

# poz_rect = pozione.get_rect()
scritta_font = pygame.font.Font('immagine/font.TTF',40)
font_surf = scritta_font.render('punteggio',False,'Black')

punti = 0
punti_font =  pygame.font.Font('immagine/font.TTF',40)
punti_img = punti_font.render(str(punti),False,'Black')
vaso = Vaso(screen,[225,585],[175,175])
# pozione = Pozione([70,70],vaso)
# moneta = Moneta([65,65],vaso,punti)

oggetti = []
pozioni = []
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
        cosa = randint(0,2)
        if cosa == 0 :
             oggetti.append(Moneta([68,68]))
        if cosa == 1:
             oggetti.append(Moneta2([68,68]))
        # else:
        #      pozioni.append(Pozione([70,70]))
             
        min = 1* fps
        max = 2 * fps
        timer = randint(min, max)
    timer -= 1

    togliere = []
    for i, oggetto in enumerate(oggetti):
        if oggetto.update(screen):
            togliere.append(i)
        print(len(oggetti))
        if oggetto.rect.colliderect(vaso.rect) and oggetto.rect.centerx>vaso.rect.left and oggetto.rect.centerx<vaso.rect.right and oggetto.rect.top<vaso.rect.top:
            togliere.append(i)
            punti += 1
            
            punti_img = punti_font.render(str(punti),False,'Black')
        else:
            oggetto.draw(screen)
    for el in togliere[::-1]:
        oggetti.pop(el)
        print(len(oggetti))
        print()
           
                
            

    
    screen.blit(punti_img,(270,35))
    screen.blit(base,(0,740))
    # disegno vaso

    vaso.draw()
    screen.blit(font_surf,(5,30))
    
    
    

   # screen.blit(vaso,(225,570))

    pygame.display.flip() 
    clock.tick(fps) 