import game.constants as c

class CharacterImg:
    hovered=False
    def __init__(self, name, pos,img,pygame,story):
        self.name=name
        self.pos=pos
        self.img=img
        self.pygame=pygame
        self.myimage = self.pygame.image.load(img)
        self.mystory=self.pygame.image.load(story)
        self.width=self.myimage.get_width()
        self.heigh=self.myimage.get_height()

    def load_img(self):
        screnw= c.SCREENWIDTH/700
        wid= round(self.width/screnw)
        hei=round(self.heigh/screnw)
        self.myimage = self.pygame.transform.scale(self.myimage, (wid,hei))
        self.image_rect=  self.myimage.get_rect(topleft=self.pos)
        c.GAME_DISPLAY.blit(self.myimage, self.pos)

    def show_story(self):
        storyw = c.SCREENWIDTH / 700
        storyh = c.SCREENWIDTH / 700
        posstory= (c.SCREENWIDTH/4,c.SCREENHEIGHT/2)
        wid = round(self.mystory.get_width() / storyw)
        hei = round(self.mystory.get_height() / storyh)
        mystory = self.pygame.transform.scale(self.mystory, (wid, hei))
        c.GAME_DISPLAY.blit(mystory, posstory)
