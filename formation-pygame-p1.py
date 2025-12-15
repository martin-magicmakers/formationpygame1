import pygame, sys
from pygame.locals import QUIT
import time

pygame.init()

fenetre = pygame.display.set_mode((400,300))

pygame.display.set_caption("mon jeu Pygame")

FPS = 60

horloge = pygame.time.Clock()

def dessiner():
    fenetre.fill("#ABCDEF")
    
    pygame.draw.rect(fenetre, "#FEDCBA", (50, 20, 110, 100))
    pygame.draw.rect(fenetre, "#123456", (60, 30, 30, 10))
    pygame.draw.rect(fenetre, "#123456", (120, 30, 30, 10))
    pygame.draw.rect(fenetre, "red", (60, 80, 30, 30))
    pygame.draw.rect(fenetre, "red", (120, 80, 30, 30))
    pygame.draw.rect(fenetre, "red", (90, 100, 30, 10)) 

    pygame.draw.ellipse(fenetre, "black", (70, 40, 20, 8))
    pygame.draw.ellipse(fenetre, "black", (130, 40, 20, 8))

    pygame.draw.circle(fenetre, "blue", (105, 55), 10)

    pygame.draw.line(fenetre, "brown", (55, 45),(105, 70),2)
    pygame.draw.line(fenetre, "brown", (55, 55),(105, 70),2)
    pygame.draw.line(fenetre, "brown", (55, 65),(105, 70),2)
    pygame.draw.line(fenetre, "brown", (55, 75),(105, 70),2)
    pygame.draw.line(fenetre, "brown", (155, 45),(105, 70),2)
    pygame.draw.line(fenetre, "brown", (155, 55),(105, 70),2)
    pygame.draw.line(fenetre, "brown", (155, 65),(105, 70),2)
    pygame.draw.line(fenetre, "brown", (155, 75),(105, 70),2)
    pygame.display.update()



while True:

    temps = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        dessiner()
        horloge.tick(FPS)
    #print("Duree en sec : ", time.time() - temps)
    
    pygame.display.update()