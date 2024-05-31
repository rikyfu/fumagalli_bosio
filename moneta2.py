from random import randint
import pygame
class Moneta2:

    def __init__(self,size) :
        
       
        self.image = pygame.image.load('immagine/moneta2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(size[0], size[1]))

        self.rect = pygame.Rect(randint(0,530),-10,size[0],size[1])
        self.speed_y = randint(7,8)
        
       
   
    def update(self, screen):
        self.rect.y += self.speed_y 

        if self.rect.y >=  screen.get_height():
            return True 
           



                   
           
    def draw(self, screen):
        screen.blit(self.image, self.rect)