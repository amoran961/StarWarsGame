import game.constants as c

class CharacterImg:
    hovered=False
    def __init__(self, name, pos,img,pygame,screen, story):
        self.name=name
        self.pos=pos
        self.img=img
        self.screen=screen
        self.pygame=pygame
        self.myimage = self.pygame.image.load(img)
        self.mystory=self.pygame.image.load(story)
    def load_img(self):
        screnw= c.SCREENWIDTH/700
        wid= round(self.myimage.get_width()/screnw)
        hei=round(self.myimage.get_height()/screnw)
        self.myimage = self.pygame.transform.scale(self.myimage, (wid,hei))
        self.image_rect=  self.myimage.get_rect(topleft=self.pos)
        self.screen.blit(self.myimage, self.pos)

    def show_story(self):
        screnw = c.SCREENWIDTH / 700
        wid = round(self.mystory.get_width() / screnw)
        hei = round(self.mystory.get_height() / screnw)
        mystory = self.pygame.transform.scale(self.mystory, (wid, hei))
        self.screen.blit(mystory, self.pos)


