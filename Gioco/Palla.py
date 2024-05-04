import pyxel
import random as rd
from math import copysign, ceil

screenx = 750
screeny= 420

#Palla
class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.speedX = -1.5
        self.speedY = -0.5
        self.r = 3
        self.out_of_bounds = False
        self.spawn = 0
        self.directionY = 1
        self.point1 = 0
        self.point2 = 0
        self.u = 41
        self.v = 1
        self.w = 7
        self.h = 7

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.u, self.v, self.w, self.h)

    def update(self):
        self.x += self.speedX
        self.y += self.speedY
        #Aumenta la velocità col tempo
        timerTime = 1
        if timerTime == 1:
            timerTime = 0
            timerTime = timerTime + 1
            if self.speedX > 0:
                self.speedX = self.speedX + 0.0015
            else:
                self.speedX = self.speedX - 0.0015
            if self.speedY > 0:
                self.speedY = self.speedY + 0.0015
            else:
                self.speedY = self.speedY - 0.0015
        
        if self.x + self.r >= screenx - 73:
            self.out_of_bounds = True
            self.spawn = 1
            pyxel.play(3,62)

        elif self.x - self.r <= 71:
            self.out_of_bounds = True
            self.spawn = -1
            pyxel.play(3,62)
        
        elif self.y - self.r <= 50:
            self.speedY = self.speedY * -1
            self.speedX = self.speedX * 1
            self.directionY = -1
            pyxel.play(3,63)
            
        elif self.y + self.r >= screeny - 55:
            self.speedY = self.speedY * -1
            self.speedX = self.speedX * 1 
            self.directionY = 1
            pyxel.play(3,63)
        #print(self.directionY)

        if timerTime == 1000:
            timerTime = 0
            if self.speedX > 0:
                self.speedX = self.speedX + 0.15
            elif self.speedX < 0:
                self.speedX = self.speedX - 0.15



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
            m = rd.randint(-1,1)
            
            #Primo segmento
            #Se sia la palla e il paddle salgono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == 1 
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            #Se la palla sta salendo e il paddle scendendo
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == 1 
            and obj.direction == -1
            ): 
                if player:
                    self.speedX = self.speedX*-1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se la palla sta scendendo e il paddle salendo
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == -1 
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1    
                    return True
                
            #Se sia il paddle e la palla stanno scendendo 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == -1 
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = -1
                    return True
            
            #Secondo segmento
            #Se stanno salendo entrambi
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            #Se il paddle sale e la palla scende
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se il paddle scende e la palla sale
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            # Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = -1
                    return True
            
            #Terzo Segmento
            #Se salgono entrambi
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)*m
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            # Se il paddle scende e la palla sale
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*m
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se il paddle sale e la palla scende
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*m
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*m
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = -1
                    return True

            #Quarto segmento
            #Se entrambi salgono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            #Se il paddle scende e la palla sale 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
                
            #Se il paddle sale e la palla scende
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Quinto segmento
            #Se entrambi salgono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            #Se il paddle scende e la palla sale 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se il paddle sale e la palla scende 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se il paddle è fermo
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and (self.directionY == -1 or self.directionY == 1)
            and obj.direction == 0
            ):
                if player:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * 1
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

            #Primo segmento
            #Se sia la palla e il paddle salgono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == 1 
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            #Se la palla sta salendo e il paddle scendendo
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == 1 
            and obj.direction == -1
            ): 
                if player2:
                    self.speedX = self.speedX*-1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se la palla sta scendendo e il paddle salendo
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == -1 
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1    
                    return True
                
            #Se sia il paddle e la palla stanno scendendo 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 8
            and self.directionY == -1 
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*n
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = -1
                    return True
            
            #Secondo segmento
            #Se stanno salendo entrambi
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            #Se il paddle sale e la palla scende
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se il paddle scende e la palla sale
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            # Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 16
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = -1
                    return True
            
            #Terzo Segmento
            #Se salgono entrambi
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)*m
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            # Se il paddle scende e la palla sale
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*m
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se il paddle sale e la palla scende
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*m
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 24
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)*m
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = -1
                    return True

            #Quarto segmento
            #Se entrambi salgono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            #Se il paddle scende e la palla sale 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
                
            #Se il paddle sale e la palla scende
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 32
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-1.5)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Quinto segmento
            #Se entrambi salgono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == 1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * 1
                    self.directionY = 1
                    return True
            
            #Se il paddle scende e la palla sale 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == 1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se il paddle sale e la palla scende 
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == -1
            and obj.direction == 1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY+2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = 1
                    return True
            
            #Se entrambi scendono
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and self.directionY == -1
            and obj.direction == -1
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    if (self.speedY == 0):
                        self.speedY = (self.speedY-2)
                    else:
                        self.speedY = self.speedY * -1
                    self.directionY = -1
                    return True
            
            #Se il paddle è fermo
            if (
            sub_ball_x + self.r >= obj.x
            and sub_ball_x - self.r <= obj.x + obj.w
            and sub_ball_y + self.r >= obj.y
            and sub_ball_y - self.r <= obj.y + 40
            and (self.directionY == -1 or self.directionY == 1)
            and obj.direction == 0
            ):
                if player2:
                    self.speedX = self.speedX * -1
                    self.speedY = self.speedY * 1
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
                    self.speedY = self.speedY * -1
                    if self.directionY == -1:
                        self.directionY = 1
                    elif self.directionY == 1:
                        self.directionY = -1
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
                    self.speedY = self.speedY * -1
                    if self.directionY == -1:
                        self.directionY = 1
                    elif self.directionY == 1:
                        self.directionY = -1
                    return True
            return False
    
    #Respawn Palla
    def Respawn_Ball(self):
        if self.out_of_bounds == True and self.spawn == 1:
            self.x = (screenx/2)
            self.y = (screeny/2)
            self.speedX = -1.5
            self.speedY = -0.5
            self.out_of_bounds = False
            self.point1 = self.point1 + 1
            self.directionY= 1
        elif self.out_of_bounds == True and self.spawn == -1:
            self.x = (screenx/2)
            self.y = (screeny/2)
            self.speedX = 1.5
            self.speedY = 0.5
            self.out_of_bounds = False
            self.point2 = self.point2 + 1
            self.directionY = -1
        self.u = 41
        self.v = 1
        self.spawn = 0
    
    #Cambiare colore alla palla
    def Change_Color(self):
        if (self.speedX >= 2 or self.speedX <= -2):
            self.u = 49
            self.v = 1
        elif (self.speedX >= 3 or self.speedX <= -3):
            self.u = 41
            self.v = 9
        elif(self.speedX >= 4 or self.speedX <= -4):
            self.u = 49
            self.v = 9
        elif(self.speedX >= 5 or self.speedX <= -5):
            self.u = 57
            self.v = 1