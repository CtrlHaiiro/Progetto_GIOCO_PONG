import pyxel
import pong


class Start:
    def __init__(self):
        pyxel.init(screenx, screeny, display_scale=2, title = "Screen", fps = 60)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y
        pyxel.mouse(visible=True)
        if pyxel.btn(pyxel.KEY_H):
            pyxel.play(0,61)
            pong()

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(screenx/2,screeny/2,10,6)

screenx = 750
screeny= 420

Start()