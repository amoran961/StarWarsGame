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
    gameDisplay= pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    pygame.display.set_caption('Star Wars')
    clock= pygame.time.Clock()
    clip = VideoFileClip('intro.mp4')
    newclip = clip.resize((SCREENWIDTH,SCREENHEIGHT))
    newclip.preview(fps=15)
    pygame.display.update()
    game_menu(gameDisplay,clock)
    pygame.quit()
    quit()

def game_menu(gameDisplay,clock):
    intro = True
    font_type = None
    font_size=50
    font_color = (255, 255, 255)
    font = pygame.font.SysFont(font_type, font_size)
    menu_font = pygame.font.Font(None, 40)
    file = "menu.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    bg = pygame.image.load("menu.png")
    bg = pygame.transform.scale(bg,(SCREENWIDTH,SCREENHEIGHT))
    op = game.menu.Option("New game", (SCREENWIDTH/20, SCREENHEIGHT/15),gameDisplay,menu_font)
    options = [op]
    state="MENU"
    while intro and  pygame.mixer.music.get_busy:

        if (state=="MENU"):
            pygame.mixer.music.unpause()
            gameDisplay.blit(bg, (0, 0))

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw(gameDisplay,menu_font)

        for event in pygame.event.get():
            print(event)
            mpos= pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for option in options:
                    if option.rect.collidepoint(pygame.mouse.get_pos()):
                        state="SELECT_CHAR"

        if (state == "SELECT_CHAR"):
            bg = pygame.image.load("select.png")
            bg = pygame.transform.scale(bg, (SCREENWIDTH, SCREENHEIGHT))
            gameDisplay.blit(bg, (0, 0))
            op1= game.select.CharacterImg("Luke",(SCREENWIDTH/10,SCREENHEIGHT/20),"luke_select.png",pygame,gameDisplay)
            op1.load_img()
            pygame.display.update()
            clock.tick(15)


        pygame.display.update()
        clock.tick(15)

