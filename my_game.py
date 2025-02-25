import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Sapoo Game")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)
        pyxel.text(70, 60, "Start", pyxel.COLOR_BLACK)
        pyxel.text(70, 50, "Quit", pyxel.COLOR_BLACK)
        
