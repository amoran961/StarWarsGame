import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from win32api import GetSystemMetrics
import pygame

SCREENWIDTH = GetSystemMetrics(0)
SCREENHEIGHT = GetSystemMetrics(1)


def start_game():

    pygame.init()
    gameDisplay= pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    pygame.display.set_caption('Star Wars')
    clock= pygame.time.Clock()
    clip = VideoFileClip('intro.mp4')
    newclip = clip.resize((SCREENWIDTH,SCREENHEIGHT))
    newclip.preview()
    pygame.display.update()


    game_intro(gameDisplay,clock)
    game_loop(clock)
    pygame.quit()
    quit()



def game_loop(clock):
    crashed= False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed =True
            print(event)
        pygame.display.update()
        clock.tick(60)


def game_intro(gameDisplay,clock):
    intro = True

    bg = pygame.image.load("menu.png")
    bg = pygame.transform.scale(bg,(SCREENWIDTH,SCREENHEIGHT))
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

        pygame.display.update()
        clock.tick(15)

