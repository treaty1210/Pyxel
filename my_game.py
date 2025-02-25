import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Sapoo Game")
        pyxel.mouse(True)
        self.number = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 30 < pyxel.mouse_x < 50 and 50 < pyxel.mouse_y < 70:
                self.number -= 1
            elif 100 < pyxel.mouse_x < 120 and 50 < pyxel.mouse_y < 70:
                self.number += 1
            elif 57 < pyxel.mouse_x < 77 and 80 < pyxel.mouse_y < 100:
                pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIME)
        pyxel.text(SCREEN_WIDTH//2-15, SCREEN_HEIGHT//2-30, "Start", pyxel.COLOR_BLACK)
        pyxel.text(75, 60, f'{self.number}', pyxel.COLOR_DARK_BLUE)
        pyxel.text(40, 60, '-', pyxel.COLOR_DARK_BLUE)
        pyxel.text(110, 60, '+', pyxel.COLOR_DARK_BLUE)
        pyxel.text(67, 90, "Quit", pyxel.COLOR_BLACK)
        
App()