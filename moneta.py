from random import randint
import pygame

class Moneta:

    def __init__(self,size) :
        
        self.image = pygame.image.load('immagine/moneta.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(size[0], size[1]))

        self.rect = pygame.Rect(randint(50,575),-20,size[0],size[1])
        self.speed_y = randint(1,6)
       
    def update(self,screen):
         self.rect.y += self.speed_y
         
         if self.rect.y >=  screen.get_height():
            self.rect.x = randint(0,screen.get_width())
            self.rect.y =  -randint(20,40)
         
    

    def draw(self,screen):
         screen.blit(self.image, self.rect)