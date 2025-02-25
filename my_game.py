import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, title="Sapoo Game")
        pyxel.mouse(True)
        self.number = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 20 < pyxel.mouse_x < 40 and 65 < pyxel.mouse_y < 85:
                self.number -= 1
            elif 100 < pyxel.mouse_x < 120 and 65 < pyxel.mouse_y < 85:
                self.number += 1
            elif 60 < pyxel.mouse_x < 80 and 90 < pyxel.mouse_y < 110:
                pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)
        pyxel.text(70, 60, "Start", pyxel.COLOR_BLACK)
        pyxel.text(70, 75, f'{self.number}', pyxel.COLOR_DARK_BLUE)
        pyxel.text(30, 75, '-', pyxel.COLOR_DARK_BLUE)
        pyxel.text(110, 75, '+', pyxel.COLOR_DARK_BLUE)
        pyxel.text(70, 100, "Quit", pyxel.COLOR_BLACK)
        
App()