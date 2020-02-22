from .actor import Actor
from .point import Point
from .grid import Grid
import pyxel

class Player(Actor):
    def __init__(self, point: Point):
        super(Player, self).__init__(point)

    def update(self, grid: Grid):
        if pyxel.btnp(pyxel.KEY_LEFT,0,1):
            self.point.x -= 2
        elif pyxel.btnp(pyxel.KEY_RIGHT,0,1):
            self.point.x += 2
        if pyxel.btnp(pyxel.KEY_UP,0,1):
            self.point.y -= 2
        elif pyxel.btnp(pyxel.KEY_DOWN,0,1):
            self.point.y += 2

    def draw(self, grid: Grid):
        pyxel.rect(self.point.x, self.point.y, 8, 8, 1)
