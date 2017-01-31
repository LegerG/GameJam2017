# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
# @type pygame 
# @type pygame 
class Personnage(pygame.sprite.Sprite):
    def __init__(self, nom):
        self.nom = nom
        self.image = pygame.image.load("Ressources/images/hero.png")
        self.hero_rect = image.get_rect()
        



