import pygame

class Moneta:

    def __init__(self, screen,pos,size) -> None:
        
        self.screen = screen
        self.image = pygame.image.load('immagine/moneta.png').convert_alpha()
        self.rect = pygame.Rect(pos[0],pos[1],size[0],size[1])
        self.image = pygame.transform.scale(self.image,(size[0], size[1]))
    
    
    def draw(self):

        self.screen.blit(self.image , self.rect)