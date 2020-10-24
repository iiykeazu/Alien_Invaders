import sys
import pygame as pg

class Mario():

    def __init__(self,screen):
        self.screen = screen

        self.image = pg.image.load('images/Mario-Standing-icon.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

def create_sky():
    pg.init()
    width = 1200
    height = 800
    bg_color = (135,206,235)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Blue Sky")
    mario = Mario(screen)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill(bg_color)
        mario.blitme()

        pg.display.flip()

create_sky()
