#Importing modules
import pygame as pg
from game.settings import Constants

class Squares():
    
    def __init__(self, xpos, ypos):
        self.hsize = (Constants.screen_width * (4/5)) * (1/7)
        self.vsize = self.hsize
        self.xpos = xpos
        self.ypos = ypos
        self.color = [0, 0, 0]
        self.font = pg.font.SysFont('Arial', 50)

    def draw_square(self, screen):
        pg.draw.rect(screen, self.color, pg.Rect(self.xpos, self.ypos, self.hsize, self.vsize), 2)
    
    def add_text(self, screen, text):
        screen.blit(self.font.render(text, True, (0,0,0)), (self.xpos + (self.hsize / 3), self.ypos + (self.vsize / 4)))
    

    def color_square(self, screen, color):
        pg.draw.rect(screen, color, pg.Rect(self.xpos, self.ypos, self.hsize, self.vsize))
        pg.draw.rect(screen, self.color, pg.Rect(self.xpos, self.ypos, self.hsize, self.vsize), 2)