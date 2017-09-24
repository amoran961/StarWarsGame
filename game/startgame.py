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


    game_menu(gameDisplay,clock)
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


def game_menu(gameDisplay,clock):
    intro = True
    font_type = None
    font_size=50
    font_color = (255, 255, 255)
    arrayit=[]
    bg = pygame.image.load("menu.png")
    bg = pygame.transform.scale(bg,(SCREENWIDTH,SCREENHEIGHT))
    file = "menu.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    font = pygame.font.SysFont(font_type, font_size)

    items=('Start game')
    posx= (SCREENWIDTH/20 )
    for index, item in enumerate(items):
        label = font.render(item, 1, font_color)

        width = label.get_rect().width
        height = label.get_rect().height
        # t_h: total width of text block

        posx =  posx + 30
        posy = (SCREENHEIGHT / 2) - (height / 2)

        arrayit.append([item, label, (width, height), (posx, posy)])

    while intro and pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(bg, (0, 0))
        for name,label,(width, height),(posx, posy) in arrayit:
            gameDisplay.blit(label, (posx, posy))

        pygame.display.flip()


        pygame.display.update()
        clock.tick(15)

