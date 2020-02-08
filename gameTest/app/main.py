import pygame
import sys

pygame.init()
SURFACE = pygame.display.set_mode((1280, 720))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
