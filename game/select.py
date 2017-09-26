import game.constants as c
class CharacterImg:

    def __init__(self, name, pos,img,pygame,screen):
        self.name=name
        self.pos=pos
        self.img=img
        self.screen=screen
        self.pygame=pygame

    def load_img(self):
        myimage = self.pygame.image.load(self.img)
        screnw= c.SCREENWIDTH/1200
        wid= round(myimage.get_width()/screnw)
        hei=round(myimage.get_height()/screnw)
        myimage = self.pygame.transform.scale(myimage, (wid,hei))
        self.screen.blit(myimage, self.pos)
        self.pygame.display.flip()



