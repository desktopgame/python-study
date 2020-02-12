import pygame
import sys
import scene 
from title import TitleScene


pygame.init()
surface = pygame.display.set_mode((32*20, 32*15))

mgr = scene.SceneManager(surface)
mgr.add('title', TitleScene())
mgr.bind('title')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            break
    if not run:
        break
    mgr.update()
    mgr.draw()
    pygame.display.update()
