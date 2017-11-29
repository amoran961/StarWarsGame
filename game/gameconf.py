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
        self.bando=""
        self.dificultad=""
        self.trivias=[]

    def generateChanges(self):
        c.DIFICULTAD=self.dificultad
        c.BANDO=self.bando
        c.MENU_IMG="menu_estrella.png"
        c.MENU_AUD = "menu_estrella.mp3"
        c.CHAR_IMG="char_estrella.png"
        c.TRIV_IMG = "triv_estrella.png"
        if(self.bando=="Rebeldes"):
            op1 = game.select.CharacterImg("caza_rebelde", ((c.SCREENWIDTH / 3), (c.SCREENHEIGHT / 18)),"caza_rebelde.png",pygame, "luke_story.png")
            op2 = game.select.CharacterImg("halcon_milenario", ((c.SCREENWIDTH / 3) + c.SCREENWIDTH/5, (c.SCREENHEIGHT / 18)), "halcon_milenario.png",pygame, "solo_story.png")
            c.CHARS=[op1,op2]
        elif(self.bando=="Imperio"):
            op1 = game.select.CharacterImg("tie_imperial", ((c.SCREENWIDTH / 3), (c.SCREENHEIGHT / 18)), "tie_imperial.png",pygame, "vader_story.png")
            op2 = game.select.CharacterImg("interdictor_imperial", ((c.SCREENWIDTH / 3) + c.SCREENWIDTH/5, (c.SCREENHEIGHT / 18)),"interdictor_imperial.png", pygame, "sidious_story.png")
            c.CHARS = [op1, op2]

    def loadImages(self):
        images = {}
        images["explosion01"] = pygame.image.load("explosion01.png").convert_alpha()
        images["explosion02"] = pygame.image.load("explosion02.png").convert_alpha()
        images["explosion03"] = pygame.image.load("explosion03.png").convert_alpha()
        images["explosion04"] = pygame.image.load("explosion04.png").convert_alpha()
        images["explosion05"] = pygame.image.load("explosion05.png").convert_alpha()
        images["explosion06"] = pygame.image.load("explosion06.png").convert_alpha()
        images["explosion07"] = pygame.image.load("explosion07.png").convert_alpha()
        images["explosion08"] = pygame.image.load("explosion08.png").convert_alpha()
        images["explosion09"] = pygame.image.load("explosion09.png").convert_alpha()
        images["explosion10"] = pygame.image.load("explosion10.png").convert_alpha()
        images["explosion11"] = pygame.image.load("explosion11.png").convert_alpha()
        images["explosion12"] = pygame.image.load("explosion12.png").convert_alpha()
        images["explosion13"] = pygame.image.load("explosion13.png").convert_alpha()
        images["explosion14"] = pygame.image.load("explosion14.png").convert_alpha()
        images["explosion15"] = pygame.image.load("explosion15.png").convert_alpha()
        images["asteroid"] = pygame.image.load("asteroid.png").convert_alpha()
        images["asteroid2"] = pygame.image.load("asteroid2.png").convert_alpha()
        if (c.BANDO == "Rebeldes"):
            images["enemy1"] = pygame.image.load("enemy_imperial1.png").convert_alpha()
            images["enemy2"] = pygame.image.load("enemy_imperial2.png").convert_alpha()
            images["enemy3"] = pygame.image.load("enemy_imperial3.png").convert_alpha()
            images["cruiser"] = pygame.image.load("cruiser_imperial.png").convert_alpha()
        elif (c.BANDO == "Imperio"):
            images["enemy1"] = pygame.image.load("enemy_rebelde1.png").convert_alpha()
            images["enemy2"] = pygame.image.load("enemy_rebelde2.png").convert_alpha()
            images["enemy3"] = pygame.image.load("enemy_rebelde3.png").convert_alpha()
            images["cruiser"] = pygame.image.load("cruiser_rebelde.png").convert_alpha
        images["ocean"] = pygame.image.load("ocean_texture.png").convert()
        images["missile"] = pygame.image.load("missile.png").convert_alpha()
        images["projectile"] = pygame.image.load("projectile.png").convert()
        images["projectile"].set_colorkey((0, 0, 0))
        images["gameOver"] = pygame.image.load("game_over.png").convert()
        images["gameOver"].set_colorkey((0, 0, 0))
        return images

    def loadSounds(self):
        sounds = {}
        sounds["explosion"] = pygame.mixer.Sound("explosion.ogg")
        sounds["plane"] = pygame.mixer.Sound("plane.ogg")
        sounds["shoot"]=pygame.mixer.Sound("shoot.ogg")
        sounds["rocket"] = pygame.mixer.Sound("rocket.ogg")
        return sounds
