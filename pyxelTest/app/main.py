import pyxel
import stage


class App:
    grid: stage.Grid

    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        self.stage = stage.Grid(24, 32)
        for i in range(self.stage.column_count):
            self.stage.set_cell(0, i, stage.ColorSlot(None))
            self.stage.set_cell(self.stage.row_count-1, i, stage.ColorSlot(None))
        for i in range(self.stage.row_count):
            self.stage.set_cell(i, 0, stage.ColorSlot(None))
            self.stage.set_cell(i, self.stage.column_count-1, stage.ColorSlot(None))
        #pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        self.stage.update()
        self.stage.draw(160, 120)


App()
