import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from win32api import GetSystemMetrics
import pygame
import game.menu
import game.select
import game.gameconf as gc
import game.constants as c


def start_game():
    pygame.init()
    c.GAME_DISPLAY=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption('Star Wars')
    clock = pygame.time.Clock()
    clip = VideoFileClip('intro.mp4')
    newclip = clip.resize((c.SCREENWIDTH, c.SCREENHEIGHT))
    newclip.preview(fps=6)
    pygame.display.update()
    game_menu(clock)
    pygame.quit()
    quit()


def game_menu(clock):
    intro = True

    menu_font = pygame.font.Font(None, 40)
    file = c.MENU_AUD
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    state = "MENU"

    while intro and pygame.mixer.music.get_busy:
        options = []
        if (state == "MENU"):
            pygame.mixer.music.unpause()
            bg = pygame.image.load(c.MENU_IMG)
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            op = game.menu.Option("New game", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 15), c.GAME_DISPLAY, menu_font)
            op2 = game.menu.Option("Quit", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 1.2), c.GAME_DISPLAY, menu_font)
            options = [op, op2]
            c.GAME_DISPLAY.blit(bg, (0, 0))


        if (state == "SELECT_CHAR"):
            bg = pygame.image.load(c.CHAR_IMG)
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            c.GAME_DISPLAY.blit(bg, (0, 0))

            opback = game.menu.Option("Back", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 1.2), c.GAME_DISPLAY, menu_font)

            for ch in c.CHARS:
                ch.load_img()

            options=[opback]

            for char in c.CHARS:
                if char.image_rect.collidepoint(pygame.mouse.get_pos()):
                    char.show_story()
        if (state=="TRIVIA"):

            bg = pygame.image.load(c.TRIV_IMG)
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            c.GAME_DISPLAY.blit(bg, (0, 0))
            triviafact= gc.TriviaFactory()
            trivia=triviafact.retornarTrivias(c.DIFICULTAD)
            pregunta= game.menu.Option(trivia.pregunta,(c.SCREENWIDTH / 4, c.SCREENHEIGHT / 2),c.GAME_DISPLAY, menu_font)
            pregunta.rect.center=(c.SCREENWIDTH / 2, c.SCREENHEIGHT / 4)
            pregunta.draw(c.GAME_DISPLAY, menu_font)

            altheight= (c.SCREENHEIGHT / 2)
            for opt in trivia.alternativas:
                alternativa=game.menu.Option(opt,(c.SCREENWIDTH / 4, c.SCREENHEIGHT / 2),c.GAME_DISPLAY, menu_font)
                alternativa.rect.center = (c.SCREENWIDTH / 2,altheight )
                altheight=altheight- 1.5*alternativa.rect.height
                alternativa.draw(c.GAME_DISPLAY, menu_font)
                options.append(alternativa)
        if (state== "TRIVIA_CORRECTA"):
            bg = pygame.image.load(c.TRIV_IMG)
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            c.GAME_DISPLAY.blit(bg, (0, 0))
            resultado = game.menu.Option("¡¡Buen trabajo!!", (c.SCREENWIDTH / 4, c.SCREENHEIGHT / 2), c.GAME_DISPLAY,
                                        menu_font)
            resultado.rect.center = (c.SCREENWIDTH / 2, c.SCREENHEIGHT / 4)

            startopt= game.select.CharacterImg("Inicio",((c.SCREENWIDTH / 2.9), (c.SCREENHEIGHT / 2.8)),"start.png",pygame, "luke_story.png")
            startopt.load_img()
            resultado.draw(c.GAME_DISPLAY, menu_font)



        elif (state== "TRIVIA_INCORRECTA"):
            bg = pygame.image.load(c.TRIV_IMG)
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            c.GAME_DISPLAY.blit(bg, (0, 0))
            resultado = game.menu.Option("Lo sentimos, no acertaste :(", (c.SCREENWIDTH / 4, c.SCREENHEIGHT / 2), c.GAME_DISPLAY,
                                        menu_font)
            resultado.rect.center = (c.SCREENWIDTH / 2, c.SCREENHEIGHT / 4)
            startopt = game.select.CharacterImg("Inicio", ((c.SCREENWIDTH / 2.9), (c.SCREENHEIGHT / 2.8)), "start.png",
                                                pygame, "luke_story.png")
            startopt.load_img()
            resultado.draw(c.GAME_DISPLAY, menu_font)


        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw(c.GAME_DISPLAY, menu_font)

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if state == "TRIVIA":
                    for option in options:
                        if option.rect.collidepoint(pygame.mouse.get_pos()) and trivia.contestar(option.text):
                            state = "TRIVIA_CORRECTA"
                        elif option.rect.collidepoint(pygame.mouse.get_pos()) and trivia.contestar(option.text)==False:
                            state = "TRIVIA_INCORRECTA"

                if state=="SELECT_CHAR":
                    for char in c.CHARS:
                        if char.image_rect.collidepoint(pygame.mouse.get_pos()):
                            state="TRIVIA"
                            c.SELECTED_CHAR=char.name

                for option in options:
                    if option.rect.collidepoint(pygame.mouse.get_pos()) and option.text=="New game":
                        state = "SELECT_CHAR"
                    elif option.rect.collidepoint(pygame.mouse.get_pos()) and option.text=="Quit":
                        pygame.quit()
                        quit()
                    elif option.rect.collidepoint(pygame.mouse.get_pos()) and option.text == "Back":
                        state="MENU"

            pygame.display.update()


        pygame.display.update()
        clock.tick(15)