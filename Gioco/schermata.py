import pyxel
import jumpman


class Start:
    def __init__(self, jumpman):
        pyxel.init(screenx, screeny, display_scale=2, title = "Screen", fps = 60)
        self.jumpman = jumpman()

    def update(self):
        self.x = pyxel.mouse_x
        self.y = pyxel.mouse_y

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(screenx/2,screeny/2,10,6)
        pyxel.rect(self.x,self.y,8,8,7)

    def start(self):
        if self.x == screenx/2 and self.y == screeny/2 and pyxel.MOUSE_BUTTON_LEFT:
            jumpman.App()

screenx = 750
screeny= 420

Start()