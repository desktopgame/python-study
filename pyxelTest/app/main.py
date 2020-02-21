import pyxel
import stage


class App:
    grid: stage.Grid

    def __init__(self):
        pyxel.init(160, 120, caption="Hello Pyxel")
        self.stage = stage.Grid(24, 32)
        #pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        for i in range(self.stage.row_count):
            for j in range(self.stage.column_count):
                self.stage[i][j].update()
                self.stage[i][j].draw()


App()
