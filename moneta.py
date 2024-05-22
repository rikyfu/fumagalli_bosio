from random import randint
import pygame

class Moneta:

    def __init__(self,screen,size) :
        
        self.screen = screen
        self.image = pygame.image.load('immagine/moneta.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(size[0], size[1]))
        
        self.x = randint(0,self.screen.get_width())
        self.y = -randint(20,40)
        self.speed_y = randint(1,6)

        self.rect = pygame.Rect(self.x,self.y,size[0],size[1])
       
    def update(self):
         self.y += self.speed_y
         if self.y >=  self.screen.get_height():
            self.x = randint(0,self.screen.get_width())
            self.y =  -randint(20,40)
         
    

    def draw(self):
         self.screen.blit(self.image, self.rect)