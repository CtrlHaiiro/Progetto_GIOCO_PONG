import pyxel
import random as rd
from math import copysign, ceil

### TO DO LIST: ###
# Aggiungi collisione paddle con campo
# Aggiungi sistema punteggio
# Soundtrack
# Sound effects
# Grafica sfondo(?)
# Balancing
# Player 3 e 4 Sprite
# Altro?
# Git Push o Commit non funge

#Giocatore 1 Ver
class Player1:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.w = 8
        self.h = 40
        self.direction = 0

    def update(self):
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
            self.y = self.y - 3
            self.direction = 1

        if pyxel.btn(pyxel.KEY_F) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.y = self.y + 3
            self.direction = 2

        if pyxel.btn(pyxel.KEY_G)or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.x = self.x + 3
            self.direction = 3

        if pyxel.btn(pyxel.KEY_D)or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.x = self.x - 3
            self.direction = 4

    def draw(self):
        pyxel.rectb(self.x, self.y,8,8,9)

#Giocatore 4 Small
class Player4:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8
        self.h = 8
        self.direction = 0

    def update(self):
        if pyxel.btn(pyxel.KEY_I) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_UP):
            self.y = self.y - 3
            self.direction = 1

        if pyxel.btn(pyxel.KEY_K) or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_DOWN):
            self.y = self.y + 3
            self.direction = 2

        if pyxel.btn(pyxel.KEY_J)or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_RIGHT):
            self.x = self.x - 3
            self.direction = 3

        if pyxel.btn(pyxel.KEY_L)or pyxel.btn(pyxel.GAMEPAD2_BUTTON_DPAD_LEFT):
            self.x = self.x + 3
            self.direction = 4

    def draw(self):
        pyxel.rectb(self.x, self.y,8,8,9)

#Palla
class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedX = -1.5
        self.speedY = -1.0
        self.r = 2
        self.out_of_bounds = False
        self.directionY = 0
        self.directionX = 0

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, 7)

    def update(self):
        self.x += self.speedX
        self.y += self.speedY
        if self.x + self.r >= screenx - 73:
             self.speedX = (self.speedX * -1)-0.1
             self.directionX = -1
        
            #self.out_of_bounds = True
        elif self.x - self.r <= 71:
             self.speedX = (self.speedX * -1)+0.1
             self.directionX = 1

            #self.out_of_bounds = True
        elif self.y - self.r <= 51:
             self.speedY = (self.speedY * -1)+0.1
             self.directionY = -1
            
        elif self.y + self.r >= screeny - 52:
             self.speedY = (self.speedY * -1)-0.1
             self.directionY = 1
    #Controllo collisione paddle 1

    def detect_collision_1(self, obj, player=False):
        num_steps = ceil(max(abs(self.speedX), abs(self.speedY)))
        if num_steps == 0:
            return False
        
        step_size = 1.0/num_steps
        
        for step in range(1, num_steps + 1):
            t = step * step_size
            sub_ball_x = self.x + t * self.speedX
            sub_ball_y = self.y + t *self.speedY
            n = rd.randrange(-1,2,2)
            m = rd.randint(-1,1)

            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            ):
                if player:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * -1
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            ):
                if player:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * n
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*n
                    else:
                        self.speedY = self.speedY * m
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            ):
                if player:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * n
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            ):
                if player:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * -1
                    return True
            return False
    #Controllo collisione paddle 2

    def detect_collision_2(self, obj, player2=False):
        num_steps = ceil(max(abs(self.speedX), abs(self.speedY)))
        if num_steps == 0:
            return False
        
        step_size = 1.0/num_steps
        
        for step in range(1, num_steps + 1):
            t = step * step_size
            sub_ball_x = self.x + t * self.speedX
            sub_ball_y = self.y + t *self.speedY
            n = rd.randrange(-1,2,2)
            m = rd.randint(-1,1)

            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * -1
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * n
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*n
                    else:
                        self.speedY = self.speedY * m
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * n
                    return True
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * -1
                    return True
            return False

#Controllo Collisione paddle 3 
    def detect_collision_3(self, obj, player3=False):
        num_steps = ceil(max(abs(self.speedX), abs(self.speedY)))
        if num_steps == 0:
            return False
        
        step_size = 1.0/num_steps
        
        for step in range(1, num_steps + 1):
            t = step * step_size
            sub_ball_x = self.x + t * self.speedX
            sub_ball_y = self.y + t *self.speedY
            n = rd.randrange(-1,2,2)

            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + obj.h
            ):
                if player3:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * n
                    return True
            return False

    #Controllo Collisione paddle 4
    def detect_collision_4(self, obj, player4=False):
        num_steps = ceil(max(abs(self.speedX), abs(self.speedY)))
        if num_steps == 0:
            return False
        
        step_size = 1.0/num_steps
        
        for step in range(1, num_steps + 1):
            t = step * step_size
            sub_ball_x = self.x + t * self.speedX
            sub_ball_y = self.y + t *self.speedY

            n = rd.randrange(-1,2,2)

            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + obj.h
            ):
                if player4:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * n
                    return True
            return False



#Principale 
class App:
    def __init__(self):
        pyxel.init(screenx, screeny, display_scale=2, title = "Screen", fps = 60)
        self.player = Player1(100, screeny/2 - 20)
        self.player2 = Player2(screenx - 110, screeny/2 - 20)
        self.player3 = Player3(150, screeny/2-2)
        self.player4 = Player4(screenx - 160, screeny/2-2)
        self.ball = Ball(screenx/2, screeny/2)
        pyxel.load("Assets/FILE_EDIT_PYXEL.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()
        self.player2.update()
        self.player3.update()
        self.player4.update()
        self.ball.update()
        self.check_collision_1()
        self.check_collision_2()
        self.check_collision_3()
        self.check_collision_4()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

#Collisioni   
    def check_collision_1(self):
        collision = self.ball.detect_collision_1(self.player, player=True)
        if collision:
            pass

    def check_collision_2(self):
        collision = self.ball.detect_collision_2(self.player2, player2=True)
        if collision:
            pass

    def check_collision_3(self):
        collision = self.ball.detect_collision_3(self.player3, player3=True)
        if collision:
            pass
    
    def check_collision_4(self):
        collision = self.ball.detect_collision_4(self.player4, player4=True)
        if collision:
            pass
    
    def draw(self):
        pyxel.cls(0)
        pyxel.rect(70, 50, screenx - 140, screeny -100, 7)
        pyxel.rect(71, 51, screenx - 142, screeny -102, 0)
        pyxel.rect(screenx - 73, 51, 3, screeny -102, 9)
        pyxel.rect(70, 51, 3, screeny -102, 3)
        self.player.draw()
        self.player2.draw()
        self.player3.draw()
        self.player4.draw()
        self.ball.draw()


screenx = 750
screeny= 420

App()
