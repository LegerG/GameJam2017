# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pygame

class Map(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ressources/images/map.png").convert_alpha()
        self.map_rect = image.get_rect()
        self.speed = 20
        
    def deplacer(self, direction):
        map_rect.move(direction*speed)
        
    def jump(self):
        print "SAUT"
    
    
