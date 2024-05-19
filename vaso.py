import pygame

class Vaso:

    def __init__(self, screen,pos,size) -> None:
        
        self.screen = screen
        self.image = pygame.image.load('immagine/vaso.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(150, 150))
        self.rect = pygame.Rect(pos[0],pos[1],size[0],size[1])
    
    def moveleft(self,pixels):
        
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 600
        
    
    def moveright(self,pixels):

        self.rect.x += pixels
        if self.rect.x > 650:
            self.rect.x = 0
    
    def draw(self):

        self.screen.blit(self.image , self.rect)
        
        
