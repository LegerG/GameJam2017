import pygame
from pygame.locals import *

import sys;

pygame.init()

fenetre = pygame.display.set_mode((700, 700), RESIZABLE)
image = pygame.image.load("map.png").convert()
pygame.display.flip()
rectangle = Rect(600, 12 * 16, 16, 16)
hero = pygame.image.load("hero.png").convert_alpha()
hero_rect = hero.get_rect()
scrolling_x = 0
scrolling_y = 0;
hero_rect.top = 100

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

        if (hero_rect.right <= 275 or scrolling_x >= 2767 - 700) and not (hero_rect.right > 700):
            hero_rect = hero_rect.move(speed[0], 0)
        elif hero_rect.right > 275 and scrolling_x < 2767 - 700 :
            scrolling_x += speed[0]


    elif touches[pygame.K_RIGHT] == 0 and touches[pygame.K_LEFT] == 1:
        if (hero_rect.left >= (2767 - 275) or scrolling_x < 0) and not (hero_rect.left < 0):
            hero_rect = hero_rect.move(-speed[0], 0)
            print "hero"
        elif (2767 - 275) > hero_rect.left > (700 - 275):
            scrolling_x -= speed[0]
            print "scroll"



    if touches[pygame.K_UP] == 0 and touches[pygame.K_DOWN] == 1:
        pass

    elif touches[pygame.K_UP] == 1 and touches[pygame.K_DOWN] == 0:
        pass


    if rectangle.colliderect(hero_rect):
        print "OUI"

    print hero_rect.right, scrolling_x
    fenetre.blit(image, [0, 0], [scrolling_x, scrolling_y, 800, 800])
    fenetre.blit(hero, hero_rect)



    pygame.display.update()