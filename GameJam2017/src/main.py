import pygame
from Map import *
from Personnage import *
from pygame.locals import *




pygame.init()
fenetreSize = (1000,700)
fenetre = pygame.display.set_mode((fenetreSize[0], fenetreSize[1]), RESIZABLE)
map = Map()
hero = Personnage()

pygame.display.flip()
hero = pygame.image.load("Ressources/images/Bonhomme.png").convert_alpha()
hero_rect = hero.get_rect()
hero_rect.left = fenetreSize[0] - (fenetreSize[0]/2) - (hero_rect.width/2)
#hero_rect.bottom = 600
hero_rect.top = fenetreSize[1] - (fenetreSize[1]/2) - (hero_rect.height/2)

hauteur_bg = map.map_rect.height
largeur_bg = map.map_rect.width
sortie = 0
horloge = pygame.time.Clock()

while sortie == 0:

    horloge.tick(50)

    for evenement in pygame.event.get():

        if evenement.type == pygame.QUIT:
            sortie = 1

    touches = pygame.key.get_pressed()

    if touches[pygame.K_RIGHT] == 1 and touches[pygame.K_LEFT] == 0:
        if map.scrolling_x <= largeur_bg - fenetreSize[0]:
            map.deplacer([1,0])
        else:
            pass    


    elif touches[pygame.K_RIGHT] == 0 and touches[pygame.K_LEFT] == 1:
        if map.scrolling_x <= 0:
             map.deplacer([-1,0])
        else :
            pass
            
    if touches[pygame.K_SPACE] == 1:
        map.jump()

        
        
    if map.scrolling_y < hauteur_bg - fenetreSize[1]:        
        map.deplacer([0,1])
        map.scrolling_y += 7
    else:
        pass
    
    
    fenetre.blit(map.image, map.map_rect)
    
    print hero_rect.right, map.scrolling_x, map.scrolling_y
#    fenetre.blit(map.image, [0, 0], [map.scrolling_x, map.scrolling_y, fenetreSize[0], fenetreSize[1]])
#    fenetre.blit(hero, hero_rect)



    pygame.display.update()