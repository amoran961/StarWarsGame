import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
from moviepy.video.fx.resize import resize
import pygame

pygame.init()
gameDisplay= pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption('Holi BOLAS')
clock= pygame.time.Clock()
clip = VideoFileClip('D:\intro\intro.mp4')
clip.preview()
crashed= False

while not crashed:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            crashed =True
        print(event)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()