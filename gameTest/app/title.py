import scene
import pygame
import pygame.draw as pydraw
import pygame.mouse as pymouse


class TitleScene(scene.Scene):

    def show(self):
        w, h = pygame.display.get_surface().get_size()
        self.table = [
            [0 for x in range(int(w / 32))] for y in range(int(h / 32))
        ]

    def hide(self):
        print('hide')

    def update(self):
        w, h = pygame.display.get_surface().get_size()
        btn1, btn2, btn3 = pymouse.get_pressed()
        mx, my = pymouse.get_pos()
        cx, cy = int(mx / 32), int(my / 32)
        if btn1:
            self.table[cy][cx] = 1
        elif btn3:
            self.table[cy][cx] = 0

    def draw(self, surface: pygame.Surface):
        w, h = surface.get_size()
        surface.fill((0, 0, 0))
        for i in range(int(w / 32)):
            for j in range(int(h / 32)):
                if self.table[j][i] == 1:
                    pydraw.rect(
                        surface,
                        pygame.Color(0, 255, 0, 255),
                        pygame.Rect((32 * i), (32 * j), 32, 32)
                    )

    @property
    def is_finished(self):
        return False

    @property
    def next_scene(self):
        return 'Play'
