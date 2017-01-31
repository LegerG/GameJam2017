import pygame
from pygame.locals import *
import sys

sys.path.insert(0, "../")

pygame.init()


class Objet():
    
    def __init__(self, image, pos_x, pos_y): #rajouter type et couleur
       
        self.img = pygame.image.load(image).convert()
       
        # Initialisation et affectation de l'attribut rect
        self.hauteur = self.img.get_rect().height
        self.largeur = self.img.get_rect().width
        
        self.rect = pygame.Rect(pos_x, pos_y, self.largeur, self.hauteur)
        
fenetreSize = (1000,700)
fenetre = pygame.display.set_mode((fenetreSize[0], fenetreSize[1]), RESIZABLE)
image = pygame.image.load("images/map.png").convert()
pygame.display.flip()
hero = pygame.image.load("images/Bonhomme.png").convert_alpha()
hero_rect = hero.get_rect()
hero_rect.left = fenetreSize[0] - (fenetreSize[0]/2) - (hero_rect.width/2)
#hero_rect.bottom = 600
hero_rect.top = fenetreSize[1] - (fenetreSize[1]/2) - (hero_rect.height/2)
scrolling_x = 0
scrolling_y = 0;
hauteur_bg = image.get_rect().height
largeur_bg = image.get_rect().width
piluleRouge = Objet("images/PiluleRouge2.png",700,600)

#2767 1200
speed = (20, 20)
sortie = 0
horloge = pygame.time.Clock()

while sortie == 0:

    horloge.tick(50)

    for evenement in pygame.event.get():

        if evenement.type == pygame.QUIT:
            sortie = 1

    touches = pygame.key.get_pressed()

    if touches[pygame.K_RIGHT] == 1 and touches[pygame.K_LEFT] == 0:
        if scrolling_x <= largeur_bg - fenetreSize[0]:
            scrolling_x += speed[0]
        else:
            pass    


    elif touches[pygame.K_RIGHT] == 0 and touches[pygame.K_LEFT] == 1:
        if scrolling_x <= 0:
             scrolling_x -= speed[0]
        else :
            pass
            
    if touches[pygame.K_SPACE] == 1:
        scrolling_y -= 50;

        
        
    if scrolling_y < hauteur_bg - fenetreSize[1]:
        
        
        scrolling_y += speed[1]
        scrolling_y += 7
    else:
        pass
    

    
    print hero_rect.right, scrolling_x
    fenetre.blit(image, [0, 0], [scrolling_x, scrolling_y, fenetreSize[0], fenetreSize[1]])
    fenetre.blit(hero, hero_rect)
    image.blit(piluleRouge.img, piluleRouge.rect)



    pygame.display.update()