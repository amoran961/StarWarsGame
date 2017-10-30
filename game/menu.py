class Option:
    hovered = False
    def __init__(self, text, pos,screen,menu_font):
        self.text = text
        self.pos = pos
        self.set_rect(menu_font)

    def draw(self,screen,menu_font):
        self.set_rend(menu_font)
        screen.blit(self.rend, self.rect)

    def set_rend(self, menu_font):
        self.rend = menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return (255, 250, 140)
        else:
            return (255, 255, 255)

    def set_rect(self,menu_font):
        self.set_rend(menu_font)
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def is_mouse_selection(self, posx, posy):
        pos_x=self.pos[0]
        pos_y = self.pos[1]

        if posx >= pos_x and posx <= pos_x :
            if posy >= pos_y and posy <= pos_y:
                return True
        return False