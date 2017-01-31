# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pygame

class Map(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ressources/images/map.png").convert_alpha()
        self.map_rect = self.image.get_rect()
        self.scrolling_x = self.map_rect.x
        self.scrolling_y = self.map_rect.y
        self.speed = 20
        
    def deplacer(self, direction):
        
        direction[0] *= self.speed
        direction[1] *= self.speed
        self.map_rect.move(direction)
        self.scrolling_x = self.map_rect.x
        self.scrolling_y = self.map_rect.y
        print direction

        
    def jump(self):
        print "SAUT"
        
    
    
