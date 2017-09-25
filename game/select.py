class Option:
    hovered = False

    def __init__(self, text, pos,screen,):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.set_draw(screen)


