#!/usr/bin/env python2
#encoding: windows-1252

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import pygame

class Pillule(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ressources/images/SeringueBleu.png").convert_alpha()
        self.pillue_rect = image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def effet(self):
        print "PILLULE"
