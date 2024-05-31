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

# creazione schermata di gioco--------------------------------------------------------------------
BLACK = (0,0,0)
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('il vaso di Pandora')
clock = pygame.time.Clock()
fps = 60
vel_vaso = 7

# caricamento immagini----------------------------------------------------------------------------
base = pygame.image.load('immagine/deserto1.png').convert_alpha()
base =pygame.transform.scale(base,(600, 100))
deserto = pygame.image.load('immagine/deserto.png').convert_alpha()
deserto =pygame.transform.scale(deserto,(600, 800))
faraone = pygame.image.load('immagine/faraone.png').convert_alpha()
faraone = pygame.transform.scale(faraone(300, 400))

# caricamento musiche-------------------------------------------------------------------------------
suono = pygame.mixer.Sound('coin.mp3')
pozione_suono = pygame.mixer.Sound('pozione.mp3')
sottofondo = pygame.mixer.Sound('sottofondo.mp3')
sottofondo.set_volume(0.2)
suono.set_volume(0.8)

# booleane per lo stato di gioco--------------------------------------------------------------------
pygame_active = False
pygame_regole_active = False

# creazione oggetti e scritte-----------------------------------------------------------------------
scritta_font = pygame.font.Font('immagine/font.TTF',40)
font_surf = scritta_font.render('punteggio',False,'Black')
titolo_font = pygame.font.Font('immagine/font.TTF',55)
titolo_surf = titolo_font.render('Il  vaso  di  Pandora',False,'White')
titolo_rect = titolo_surf.get_rect(center = (300,80))
space_surf = titolo_font.render('Press  Space  to  play',False,'White')
space_rect = space_surf.get_rect(center = (300,600))
monete_surf = scritta_font.render('raccogli  le  monete',False,'White')
monete_rect = monete_surf.get_rect(center = (300,270))
pozione_surf = scritta_font.render('evita  le  pozioni',False,'White')
pozione_rect = pozione_surf.get_rect(center = (300,350))
comandi_font = pygame.font.Font('immagine/font.TTF',35)
comandi_surf = comandi_font.render('muoviti  con  le  frecce  DX  e  SX',False,'White')
comandi_rect = space_surf.get_rect(center = (300,440))

# punteggio------------------------------------------------------------------------------------------
punti = 0
punti_font =  pygame.font.Font('immagine/font.TTF',40)
punti_img = punti_font.render(str(punti),False,'Black')

# creazione classi------------------------------------------------------------------------------------
vaso = Vaso(screen,[225,585],[175,175])
tavolo = Tavolo([580, 300])

bottone_gioca = Bottone(screen, 
                        [310, 650],# pos
                        [220, 100], #size
                        'gioca'
                        )

bottone_regole = Bottone(screen, 
                        [70, 650],# pos
                        [220, 100], #size
                        'regole'
                        )

# liste---------------------------------------------------------------------------------------------
oggetti = []
oggetti2 = []
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