import scene
import pygame
from pygame.draw import draw as pydraw


class TitleScene(scene.Scene):

    def show(self):
        print('show')

    def hide(self):
        print('hide')

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        pydraw.rect(surface, (78, 203, 245), (0, 0, 250, 500), 5)
        surface.fill((0, 255, 0))

    @property
    def is_finished(self):
        return False

    @property
    def next_scene(self):
        return 'Play'
