import pygame
from pygame.locals import *
import sys

sys.path.insert(0, "../")



pygame.init()
fenetreSize = (1000,700)
fenetre = pygame.display.set_mode((fenetreSize[0], fenetreSize[1]), RESIZABLE)
image = pygame.image.load("Ressources/images/map.png").convert()
pygame.display.flip()
hero = pygame.image.load("Ressources/images/hero.png").convert_alpha()
hero_rect = hero.get_rect()
scrolling_x = 0
scrolling_y = 0;
hauteur_bg = image.get_rect().height
largeur_bg = image.get_rect().width
decalement = 275
#2767 1200
speed = (20, 10)
sortie = 0
horloge = pygame.time.Clock()

while sortie == 0:

    horloge.tick(50)

    for evenement in pygame.event.get():

        if evenement.type == pygame.QUIT:
            sortie = 1

    touches = pygame.key.get_pressed()

    if touches[pygame.K_RIGHT] == 1 and touches[pygame.K_LEFT] == 0:

        if (hero_rect.right <= decalement or scrolling_x >= largeur_bg - fenetreSize[1]) and not (hero_rect.right > fenetreSize[1]):
            hero_rect = hero_rect.move(speed[0], 0)
        elif hero_rect.right > decalement and scrolling_x < largeur_bg - fenetreSize[1] :
            scrolling_x += speed[0]


    elif touches[pygame.K_RIGHT] == 0 and touches[pygame.K_LEFT] == 1:
        if (hero_rect.left >= (largeur_bg - decalement) or scrolling_x < 0) and not (hero_rect.left < 0):
            hero_rect = hero_rect.move(-speed[0], 0)
            print "hero"
        elif (2767 - 275) > hero_rect.left > (fenetreSize[1] - decalement):
            scrolling_x -= speed[0]
            print "scroll"



    if touches[pygame.K_UP] == 0 and touches[pygame.K_DOWN] == 1:

        if (hero_rect.bottom <= decalement or scrolling_y >= hauteur_bg - fenetreSize[1]) and not (hero_rect.bottom > fenetreSize[1]):
            hero_rect = hero_rect.move(0, speed[1])
        elif hero_rect.bottom > decalement and scrolling_y < hauteur_bg - fenetreSize[1] :
            scrolling_y += speed[1]

        if hero_rect.bottom > fenetreSize[1]:
            hero_rect.bottom = fenetreSize[1]


    elif touches[pygame.K_UP] == 1 and touches[pygame.K_DOWN] == 0:

        if (hero_rect.top >= (hauteur_bg - decalement) or scrolling_y < 0):
            hero_rect = hero_rect.move(0, -speed[1])
        elif hero_rect.top <= (fenetreSize[1] - decalement) or scrolling_y > 0:
            scrolling_y -= speed[1]
        elif hero_rect.bottom <= fenetreSize[1] and hero_rect.top >= fenetreSize[1] - decalement :
            hero_rect = hero_rect.move(0, -speed[1])

        if  (hero_rect.top < 0):
            hero_rect.top = 0


    print hero_rect.right, scrolling_x
    fenetre.blit(image, [0, 0], [scrolling_x, scrolling_y, fenetreSize[0], fenetreSize[1]])
    fenetre.blit(hero, hero_rect)



    pygame.display.update()