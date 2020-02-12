import pygame
import sys
import scene

from title import TitleScene

pygame.init()
surface = pygame.display.set_mode((1280, 720))

mgr = scene.SceneManager(surface)
mgr.add('title', TitleScene())
mgr.bind('title')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mgr.update()
    mgr.draw()
    pygame.display.update()
