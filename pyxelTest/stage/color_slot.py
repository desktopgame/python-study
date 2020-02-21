from .slot import *
import pyxel

class ColorSlot(Slot):
    def __init__(self, point):
        super(ColorSlot, self).__init__(point)
    
    def draw(self, x: int, y: int, w: int, h: int):
        pyxel.rect(x, y, w, h, 4)