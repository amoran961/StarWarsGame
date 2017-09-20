import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from moviepy.video.fx.resize import resize
from models.popup_menu import PopupMenu
import pygame
import sys

pygame.init()
SCREENWIDTH=1920
SCREENHEIGHT=1080
gameDisplay= pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Star Wars')
clock= pygame.time.Clock()
basicfont = pygame.font.SysFont("comicsansms", 72)
menu_data = (
    'Main',
    'Item 0',
    'Item 1',
    (
        'Things',
        'Item 0',
        'Item 1',
        'Item 2',
        (
            'More Things',
            'Item 0',
            'Item 1',
        ),
    ),
    'Quit',
)


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

clip = VideoFileClip('intro.mp4')
clip.resize(height=1080)
clip.preview()

pygame.display.update()


def game_loop():
    crashed= False
    while not crashed:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                crashed =True
            print(event)

        pygame.display.update()
        clock.tick(60)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True

    bg = pygame.image.load("menu.png")
    file = "menu.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while intro and pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bg, (0, 0))
        PopupMenu(menu_data)
        pygame.display.update()
        clock.tick(15)






game_intro()
game_loop()
pygame.quit()
quit()