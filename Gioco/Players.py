import pyxel
import random as rd
from math import copysign, ceil
from Palla import Ball

#Giocatore 1 Ver
class Player1:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.w = 8
        self.h = 40
        self.direction = 0

    def update(self):
        self.direction = 0
        if pyxel.btn(pyxel.KEY_W):
            if self.y < 53:
                pass
            else:
                self.y = self.y - 3
                self.direction = 1

        if pyxel.btn(pyxel.KEY_S):
            if self.y > (screeny-93):
                pass
            else:
                self.y = self.y + 3
                self.direction = -1
        
    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8)
        pyxel.blt(self.x, self.y+8, 0, 0, 8, 8, 8)
        pyxel.blt(self.x,self.y+16, 0, 0, 16, 8, 8)
        pyxel.blt(self.x, self.y+24, 0, 8, 0, 8, 8)
        pyxel.blt(self.x, self.y+32, 0, 8, 8, 8, 8)

#Giocatore 2 Ver
class Player2:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.w = 8
        self.h = 40
        self.direction = 0

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            if self.y < 53:
                pass
            else:
                self.y = self.y - 3
                self.direction = 1

        if pyxel.btn(pyxel.KEY_DOWN):
            if self.y > (screeny-93):
                pass
            else:
                self.y = self.y + 3
                self.direction = -1
        print(self.direction)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 16, 0, 8, 8)
        pyxel.blt(self.x, self.y+8, 0, 16, 8, 8, 8)
        pyxel.blt(self.x, self.y+16, 0, 16, 16, 8, 8)
        pyxel.blt(self.x, self.y+24, 0, 24, 0, 8, 8)
        pyxel.blt(self.x, self.y+32, 0, 24, 8, 8,8)

#Giocatore 3 Small
class Player3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.direction = 0

    def update(self):
        if pyxel.btn(pyxel.KEY_R) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            if self.y < 53:
                pass
            else:
                self.y = self.y - 3
                self.direction = 1

        if pyxel.btn(pyxel.KEY_F) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            if self.y+self.h > (screeny-56):
                pass
            else:
                self.y = self.y + 3
                self.direction = 2

        if pyxel.btn(pyxel.KEY_G)or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            if self.x+self.w > (screenx/2):
                pass
            else:
                self.x = self.x + 3
                self.direction = 3

        if pyxel.btn(pyxel.KEY_D)or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            if self.x-self.w <= 68:
                pass
            else:
                self.x = self.x - 3
                self.direction = 4
    def draw(self):
        pyxel.circb(self.x+4, self.y+4, 4, 0)
        pyxel.blt(self.x, self.y, 0, 32,8,self.w, self.h)
        

#Giocatore 4 Small
class Player4:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.directionX = 0
        self.directionY = 0

    def update(self):
        if pyxel.btn(pyxel.KEY_I) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_UP):
            if self.y < 53:
                pass
            else:
                self.y = self.y - 3
                self.direction = 1

        if pyxel.btn(pyxel.KEY_K) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN):
            if self.y+self.h > (screeny-56):
                pass
            else:
                self.y = self.y + 3
                self.direction = 2

        if pyxel.btn(pyxel.KEY_L)or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT):
            if self.x+self.w > (screenx-73):
                pass
            else:
                self.x = self.x + 3
                self.direction = 3

        if pyxel.btn(pyxel.KEY_J)or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT):
            if self.x-self.w <= (screenx/2):
                pass
            else:
                self.x = self.x - 3
                self.direction = 4

    def draw(self):
        pyxel.circb(self.x+4, self.y+4, 4, 0)
        pyxel.blt(self.x, self.y, 0, 32, 0, self.w, self.h)

screenx = 750
screeny= 420
