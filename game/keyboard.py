import pygame as pg
from game.settings import Constants

class Keys():
    def __init__(self, xpos, ypos):
        
        self.hsize = (Constants.screen_width * (5/6)) // 10
        self.vsize = (Constants.screen_height * (1/4)) // 3
        self.xpos = xpos
        self.ypos = ypos 
        self.color = [0, 0, 0]
        self.font = pg.font.SysFont('Arial', 15)
    
    def draw_rectangle(self, screen, text):
        pg.draw.rect(screen, self.color, pg.Rect(self.xpos, self.ypos, self.hsize, self.vsize), 2)
        if text != 'ENTER':
            screen.blit(self.font.render(text, True, (0,0,0)), (self.xpos + (self.hsize / 2), self.ypos + (self.vsize / 2)))
        else: 
            screen.blit(self.font.render(text, True, (0,0,0)), (self.xpos + (self.hsize / 10), self.ypos + (self.vsize / 2)))
    
    def update_rect_color(self, screen, color, text):
        pg.draw.rect(screen, color, pg.Rect(self.xpos, self.ypos, self.hsize, self.vsize))
        pg.draw.rect(screen, self.color, pg.Rect(self.xpos, self.ypos, self.hsize, self.vsize), 2)
        if text != 'ENTER':
            screen.blit(self.font.render(text, True, (255,255,255)), (self.xpos + (self.hsize / 2), self.ypos + (self.vsize / 2)))
        else: 
            screen.blit(self.font.render(text, True, (255,255,255)), (self.xpos + (self.hsize / 10), self.ypos + (self.vsize / 2)))


    def key_pressed():
        pass