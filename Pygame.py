import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((300, 300))
pygame.display.set_caption("My Game")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
pygame.draw.rect(DISPLAYSURF, (0, 255, 0), (100, 50, 20, 20))
pygame.display.update()

