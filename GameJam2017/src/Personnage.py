# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# @type pygame 
# @type pygame 
import pygame

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Ressources/images/Bonhomme.png").convert_alpha()
        self.hero_rect = image.get_rect()
        
        
        self.setup_bool()
        
    def setup_bool(self):
        self.autoriser_saut = true
        self.mort = false

