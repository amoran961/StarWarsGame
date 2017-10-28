import game.constants as c
import game.select
import game.menu
import pygame
class Trivia:
    def __init__(self, dificultad, img,res):
        self.dificultad = dificultad
        self.img = img
        self.res= res

    def showTrivia(self):
        pass

class GameConfig:
    def __init__(self):
        self.mision=""
        self.bando=""
        self.dificultad=""
        self.trivias=[]

    def generateChanges(self):

        c.DIFICULTAD=self.dificultad

        if(self.mision=="Luna de Endor"):
            c.MENU_IMG="menu_endor.png"
            c.MENU_AUD="menu_endor.mp3"
            c.CHAR_IMG="char_endor.png"
        elif(self.mision=="Estrella de la muerte"):
            c.MENU_IMG="menu_estrella.png"
            c.MENU_AUD = "menu_estrella.mp3"
            c.CHAR_IMG="char_estrella.png"

        if(self.bando=="Rebelde"):
            op1 = game.select.CharacterImg("Luke", ((c.SCREENWIDTH / 3), (c.SCREENHEIGHT / 18)),"luke_select.png",pygame, "luke_story.png")
            op2 = game.select.CharacterImg("Solo", ((c.SCREENWIDTH / 3) + c.SCREENWIDTH/5, (c.SCREENHEIGHT / 18)), "solo_select.png",pygame, "luke_story.png")
            c.CHARS=[op1,op2]
        elif(self.bando=="Imperio"):
            op1 = game.select.CharacterImg("Vader", ((c.SCREENWIDTH / 3), (c.SCREENHEIGHT / 18)), "vader_select.png",pygame, "luke_story.png")
            op2 = game.select.CharacterImg("Sidious", ((c.SCREENWIDTH / 3) + c.SCREENWIDTH/5, (c.SCREENHEIGHT / 18)),"sidious_select.png", pygame, "luke_story.png")
            c.CHARS = [op1, op2]

        if(self.dificultad=="facil"):
            pass
        elif(self.dificultad=="medio"):
            pass
        elif(self.dificultad=="dificil"):
            pass











