import imageio

imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from win32api import GetSystemMetrics
import pygame
import game.menu
import game.select

SCREENWIDTH = GetSystemMetrics(0)
SCREENHEIGHT = GetSystemMetrics(1)


def start_game():
    pygame.init()
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Star Wars')
    clock = pygame.time.Clock()
    clip = VideoFileClip('intro.mp4')
    newclip = clip.resize((SCREENWIDTH, SCREENHEIGHT))
    newclip.preview(fps=6)
    pygame.display.update()
    game_menu(gameDisplay, clock)
    pygame.quit()
    quit()


def game_menu(gameDisplay, clock):
    intro = True
    font_type = None
    font_size = 50
    font_color = (255, 255, 255)
    font = pygame.font.SysFont(font_type, font_size)
    menu_font = pygame.font.Font(None, 40)
    file = "menu.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    state = "MENU"
    while intro and pygame.mixer.music.get_busy:

        if (state == "MENU"):
            pygame.mixer.music.unpause()
            bg = pygame.image.load("menu.png")
            bg = pygame.transform.scale(bg, (SCREENWIDTH, SCREENHEIGHT))
            op = game.menu.Option("New game", (SCREENWIDTH / 20, SCREENHEIGHT / 15), gameDisplay, menu_font)
            op2 = game.menu.Option("Quit", (SCREENWIDTH / 20, SCREENHEIGHT / 1.2), gameDisplay, menu_font)
            options = [op, op2]
            gameDisplay.blit(bg, (0, 0))

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw(gameDisplay, menu_font)
        if (state == "SELECT_CHAR"):
            bg = pygame.image.load("select.png")
            bg = pygame.transform.scale(bg, (SCREENWIDTH, SCREENHEIGHT))
            gameDisplay.blit(bg, (0, 0))

            opback = game.menu.Option("Back", (SCREENWIDTH / 20, SCREENHEIGHT / 1.2), gameDisplay, menu_font)

            op1 = game.select.CharacterImg("Luke", ((SCREENWIDTH / 10) + 600, (SCREENHEIGHT / 20)), "luke_select.png",
                                           pygame, gameDisplay)
            op2 = game.select.CharacterImg("Vader", ((SCREENWIDTH / 10) + 300, (SCREENHEIGHT / 20)), "vader_select.png",
                                           pygame, gameDisplay)
            op3 = game.select.CharacterImg("Solo", ((SCREENWIDTH / 10), (SCREENHEIGHT / 20)), "solo_select.png", pygame,
                                           gameDisplay)
            op4 = game.select.CharacterImg("Sidious", ((SCREENWIDTH / 10) + 900, (SCREENHEIGHT / 20)),
                                           "sidious_select.png", pygame, gameDisplay)
            op2.load_img()
            op3.load_img()
            op1.load_img()
            op4.load_img()
            options=[opback]
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
