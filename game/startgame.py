import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from win32api import GetSystemMetrics
import pygame
import game.menu
import game.select
import game.gameconf as gc
import game.constants as c
import game.starkiller as sk
import game.fileLoader as fl


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

    menu_font = pygame.font.Font(None,25)
    file = c.MENU_AUD
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while intro and pygame.mixer.music.get_busy:
        options = []
        if (c.STATE == "MENU"):
            pygame.mixer.music.unpause()
            bg = pygame.image.load(c.MENU_IMG)
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            op = game.menu.Option("New game", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 15), c.GAME_DISPLAY, menu_font)
            op2 = game.menu.Option("Quit", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 1.2), c.GAME_DISPLAY, menu_font)
            options = [op, op2]
            c.GAME_DISPLAY.blit(bg, (0, 0))


        if (c.STATE == "SELECT_CHAR"):
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
        if (c.STATE=="TRIVIA"):

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

        if (c.STATE== "TRIVIA_CORRECTA"):
            bg = pygame.image.load(c.TRIV_IMG)
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            c.GAME_DISPLAY.blit(bg, (0, 0))
            resultado = game.menu.Option("¡¡Buen trabajo!!", (c.SCREENWIDTH / 4, c.SCREENHEIGHT / 2), c.GAME_DISPLAY,
                                        menu_font)
            resultado.rect.center = (c.SCREENWIDTH / 2, c.SCREENHEIGHT / 4)

            startopt= game.select.CharacterImg("Inicio",((c.SCREENWIDTH / 2.9), (c.SCREENHEIGHT / 2.8)),"start.png",pygame, "luke_story.png")
            startopt.load_img()
            resultado.draw(c.GAME_DISPLAY, menu_font)
        elif (c.STATE== "TRIVIA_INCORRECTA"):
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

        if (c.STATE == "EN_JUEGO"):
            if(c.MISION=="Ataque a la Estrella de la Muerte"):
                gamecf=gc.GameConfig()
                c.IMAGES = gamecf.loadImages()
                c.SOUNDS = gamecf.loadSounds()
                gameSK = sk.Game()
                gameSK.start_game()
                done = False

                while not done:
                    # --- Main event loop
                    for event in pygame.event.get():  # User did something
                        if event.type == pygame.QUIT or c.STATE=="MENU":  # If user clicked close
                            done = True  # Flag that we are done so we exit this loop

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            gameSK.shoot()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p and c.STATE == "PAUSE":
                                c.STATE = ""
                                gameSK.running=True
                            elif event.key == pygame.K_p and c.STATE != "PAUSE":
                                c.STATE = "PAUSE"
                                gameSK.running=False

                            elif event.key == pygame.K_ESCAPE:
                                if gameSK.running:
                                    gameSK.running = False
                                    c.SOUNDS["plane"].stop()
                                else:
                                    gameSK.display_help_screen = False
                                    gameSK.display_credits_screen = False

                    # --- Game logic should go here
                    if gameSK.running:
                        gameSK.run_game()
                    # First, clear the screen to white. Don't put other drawing commands
                    # above this, or they will be erased with this command.
                    c.GAME_DISPLAY.fill((255, 255, 255))

                    # --- Drawing code should go here
                    gameSK.display_frame(c.GAME_DISPLAY)
                    # --- Go ahead and update the screen with what we've drawn.
                    pygame.display.flip()

                    # --- Limit to 30 frames per second
                    clock.tick(30)
        if c.STATE=="PAUSE":
            c.GAME_DISPLAY.blit("En pausa", (100, 100))
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

                if c.STATE == "TRIVIA_CORRECTA":
                    if startopt.image_rect.collidepoint(pygame.mouse.get_pos()):
                        c.STATE="EN_JUEGO"

                elif c.STATE == "TRIVIA_INCORRECTA":
                    if startopt.image_rect.collidepoint(pygame.mouse.get_pos()):
                        c.STATE="EN_JUEGO"

                if c.STATE == "TRIVIA":
                    for option in options:
                        if option.rect.collidepoint(pygame.mouse.get_pos()) and trivia.contestar(option.text):
                            c.STATE = "TRIVIA_CORRECTA"

                        elif option.rect.collidepoint(pygame.mouse.get_pos()) and trivia.contestar(option.text)==False:
                            c.STATE = "TRIVIA_INCORRECTA"

                if c.STATE=="SELECT_CHAR":
                    for char in c.CHARS:
                        if char.image_rect.collidepoint(pygame.mouse.get_pos()):
                            c.STATE="TRIVIA"
                            c.SELECTED_CHAR=char.img

                for option in options:
                    if option.rect.collidepoint(pygame.mouse.get_pos()) and option.text=="New game":
                        c.STATE = "SELECT_CHAR"
                    elif option.rect.collidepoint(pygame.mouse.get_pos()) and option.text=="Quit":
                        pygame.quit()
                        quit()
                    elif option.rect.collidepoint(pygame.mouse.get_pos()) and option.text == "Back":
                        c.STATE="MENU"

            pygame.display.update()


        pygame.display.update()
        clock.tick(15)