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