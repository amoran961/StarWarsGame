import imageio

imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from win32api import GetSystemMetrics
import pygame
import game.menu
import game.select
import game.constants as c



def start_game():
    pygame.init()
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Star Wars')
    clock = pygame.time.Clock()
    clip = VideoFileClip('intro.mp4')
    newclip = clip.resize((c.SCREENWIDTH, c.SCREENHEIGHT))
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
    substate=""
    charname=""
    while intro and pygame.mixer.music.get_busy:

        if (state == "MENU"):
            pygame.mixer.music.unpause()
            bg = pygame.image.load("menu.png")
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            op = game.menu.Option("New game", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 15), gameDisplay, menu_font)
            op2 = game.menu.Option("Quit", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 1.2), gameDisplay, menu_font)
            options = [op, op2]
            gameDisplay.blit(bg, (0, 0))


        if (state == "SELECT_CHAR"):
            bg = pygame.image.load("select.png")
            bg = pygame.transform.scale(bg, (c.SCREENWIDTH, c.SCREENHEIGHT))
            gameDisplay.blit(bg, (0, 0))



            op1 = game.select.CharacterImg("Luke", ((c.SCREENWIDTH / 10) + 600, (c.SCREENHEIGHT / 20)), "luke_select.png",
                                           pygame, gameDisplay,"luke_story.png")
            op2 = game.select.CharacterImg("Vader", ((c.SCREENWIDTH / 10) + 300, (c.SCREENHEIGHT / 20)), "vader_select.png",
                                           pygame, gameDisplay,"luke_story.png")
            op3 = game.select.CharacterImg("Solo", ((c.SCREENWIDTH / 10), (c.SCREENHEIGHT / 20)), "solo_select.png", pygame,
                                           gameDisplay,"luke_story.png")
            op4 = game.select.CharacterImg("Sidious", ((c.SCREENWIDTH / 10) + 900, (c.SCREENHEIGHT / 20)),
                                           "sidious_select.png", pygame, gameDisplay,"luke_story.png")
            opback = game.menu.Option("Back", (c.SCREENWIDTH / 20, c.SCREENHEIGHT / 1.2), gameDisplay, menu_font)
            op2.load_img()
            op3.load_img()
            op1.load_img()
            op4.load_img()
            options=[opback]
            chars=[op1,op2,op3,op4]

            for char in chars:
                if char.image_rect.collidepoint(pygame.mouse.get_pos()):
                    char.show_story()

        for option in options:
            if option.rect.collidepoint(pygame.mouse.get_pos()):
                option.hovered = True
            else:
                option.hovered = False
            option.draw(gameDisplay, menu_font)

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if state=="SELECT_CHAR":
                    pass

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