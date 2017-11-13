import game.constants as c
import game.select
import game.menu
import pygame
class Trivia:
    def __init__(self,pregunta,alternativas,res):
        self.pregunta=pregunta
        self.alternativas =alternativas
        self.res= res
    def contestar(self,respuesta):
        result=False
        if(self.res==respuesta):
            result=True
        return result
class TriviaFactory():
    def retornarTrivias(self,dificultad):
        trivia =""
        if (dificultad == "Fácil"):
            pregunta = "¿En qué planeta se creó el Ejército Clon?"
            alternativas = ["d. Kamino", "c. Utapau", "b. Ryloth", "a. Mustafar"]
            res = "d. Kamino"
            trivia = Trivia(pregunta, alternativas, res)
        elif (dificultad == "Intermedio"):
            pregunta = "¿Quién es más loco, el loco o el loco que sigue al loco? Fue una frase pronunciada por"
            alternativas = ["d. Qui-Gon Jinn", "c. Obi-Wan Kenobi", "b. Han Solo", "a. Yoda"]
            res = "b. Han Solo"
            trivia = Trivia(pregunta, alternativas, res)
        elif (dificultad == "Difícil"):
            pregunta = "¿De qué raza es el cazarrecompensas que asesina Han Solo en la Cantina de Mos Eisley?"
            alternativas = ["d. Sullustana", "c. Rodiana", "b. Saleucami", "a. Twi'lek"]
            res = "c. Rodiana"
            trivia = Trivia(pregunta, alternativas, res)

        return trivia

class GameConfig:
    def __init__(self):
        self.mision=""
        self.bando=""
        self.dificultad=""
        self.trivias=[]

    def generateChanges(self):

        c.DIFICULTAD=self.dificultad

        if(self.mision=="Asalto a la luna de Endor"):
            c.MENU_IMG="menu_endor.png"
            c.MENU_AUD="menu_endor.mp3"
            c.CHAR_IMG="char_endor.png"
            c.TRIV_IMG = "triv_endor.png"
        elif(self.mision=="Ataque a la Estrella de la Muerte"):
            c.MENU_IMG="menu_estrella.png"
            c.MENU_AUD = "menu_estrella.mp3"
            c.CHAR_IMG="char_estrella.png"
            c.TRIV_IMG = "triv_estrella.png"

        if(self.bando=="Rebeldes"):
            op1 = game.select.CharacterImg("Luke", ((c.SCREENWIDTH / 3), (c.SCREENHEIGHT / 18)),"luke_select.png",pygame, "luke_story.png")
            op2 = game.select.CharacterImg("Solo", ((c.SCREENWIDTH / 3) + c.SCREENWIDTH/5, (c.SCREENHEIGHT / 18)), "solo_select.png",pygame, "solo_story.png")
            c.CHARS=[op1,op2]
        elif(self.bando=="Imperio"):
            op1 = game.select.CharacterImg("Vader", ((c.SCREENWIDTH / 3), (c.SCREENHEIGHT / 18)), "vader_select.png",pygame, "vader_story.png")
            op2 = game.select.CharacterImg("Sidious", ((c.SCREENWIDTH / 3) + c.SCREENWIDTH/5, (c.SCREENHEIGHT / 18)),"sidious_select.png", pygame, "sidious_story.png")
            c.CHARS = [op1, op2]













