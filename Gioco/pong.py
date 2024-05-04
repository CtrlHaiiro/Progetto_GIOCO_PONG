import pyxel
import time 
import random as rd
from math import copysign, ceil
from Palla import Ball
from Players import Player1, Player2, Player3, Player4

### TO DO LIST: ###
# DONE - Aggiungi collisione paddle con campo
# DONE - Aggiungi sistema punteggio
# DONE - Soundtrack
# DONE - Sound effects
# RIVALUTATO | N/A - Grafica sfondo(?)
# TO DO - Balancing
# DONE - Player 3 e 4 Sprite
# RIVALUTATO | N/A - Allargare l'area di Player 3 e 4??
# IN PROGRESS - Finire le collisioni tra palla e paddle(paddle 1 e 2 fatti)(2/4)
# TO DO - Aggiugere una schermata di scelta modalità
# IN PROGRESS - Sistemare i Player 3 e 4
# DONE Cambiare colore alla palla 

#Principale 
class App:
    def __init__(self):
        #pyxel.init(screenx, screeny, display_scale=2, title = "Screen", fps = 60)
        self.player = Player1(100, screeny/2 - 20)
        self.player2 = Player2(screenx - 110, screeny/2 - 20)
        self.player3 = Player3(150, screeny/2-2)
        self.player4 = Player4(screenx - 160, screeny/2-2)
        self.ball = Ball(screenx/2, screeny/2)
        pyxel.load("Assets/FILE_EDIT_PYXEL.pyxres")
        pyxel.playm(0,loop=True)
        pyxel.run(self.update, self.draw)

    #Collisioni   
    def check_collision_1(self):
        collision = self.ball.detect_collision_1(self.player, player=True)
        if collision:
            pyxel.play(3,63)
            pass

    def check_collision_2(self):
        collision = self.ball.detect_collision_2(self.player2, player2=True)
        if collision:
            pyxel.play(3,63)
            pass

    def check_collision_3(self):
        collision = self.ball.detect_collision_3(self.player3, player3=True)
        if collision:
            pyxel.play(3,63)
            pass
    
    def check_collision_4(self):
        collision = self.ball.detect_collision_4(self.player4, player4=True)
        if collision:
            pyxel.play(3,63)
            pass

    def update(self):
        self.ball.update()
        self.player.update()
        self.player2.update()
        self.player3.update()
        self.player4.update()
        self.check_collision_1()
        self.check_collision_2()
        self.check_collision_3()
        self.check_collision_4()
        self.respawn()
        self.change_color()
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()


    #Respawn palla
    def respawn(self):
        resp = self.ball.Respawn_Ball()
        if resp:
            pass
    #Colore Palla
    def change_color(self):
        col = self.ball.Change_Color()
        if col:
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
        pyxel.text((screenx/2)-20,30,str(self.ball.point1),7)
        pyxel.text((screenx/2)+20,30,str(self.ball.point2),7)

screenx = 750
screeny= 420

App()