import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Sapoo Game")

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
