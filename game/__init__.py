#Import Modules
from random import choice
from numpy import square
import pygame as pg
import sys
from game.settings import Constants, Words
from game.keyboard import Keys
from game.squares import Squares

#Sets up Game class
class Game():
    
    def __init__(self): #Initializes pygame, sets up various pygame objects/screen
        #SET UP PYGAME STUFF
        pg.init()
        self.screen = pg.display.set_mode((Constants.screen_width, Constants.screen_height))
        self.screen.fill(Constants.bg_color)
        #Creates 2 lists that contain the x and y positions of the keys on the keyboard, then creates a list of Keys objects
        self.key_xpositions = [(1/12) * (Constants.screen_width) + k * ((Constants.screen_width * 5/6) / 10) + (7*k) for k in range(10)]
        self.key_ypositions = [(3/4) * (Constants.screen_height) + k * ((Constants.screen_height * 1/4) / 3) - 30 + (5*k) for k in range(3)]
        self.keys_list = [Keys(self.key_xpositions[key], self.key_ypositions[0]) for key in range(len(self.key_xpositions) - 1)] + [Keys(self.key_xpositions[key], self.key_ypositions[1]) for key in range(len(self.key_xpositions) - 1)] + [Keys(self.key_xpositions[key], self.key_ypositions[2]) for key in range(len(self.key_xpositions) - 1)]
        iterator = 0
        #Draws the keys using the objects in the self.keys_list 
        for key in self.keys_list:
            key.draw_rectangle(self.screen, Constants.keys[iterator])
            ## BELOW IS A TEST CASE USED TO TEST MY CODE
            #if iterator % 2 == 0:
            #    key.update_rect_color(self.screen, Constants.missing_color, Constants.keys[iterator])
            iterator += 1
        self.square_xpositions = [(1/10) * (Constants.screen_width) + k * ((Constants.screen_width * 3/4) / 5) + (20*k) for k in range(5)] + [(1/10) * (Constants.screen_width) + k * ((Constants.screen_width * 3/4) / 5) + (20*k) for k in range(5)] + [(1/10) * (Constants.screen_width) + k * ((Constants.screen_width * 3/4) / 5) + (20*k) for k in range(5)] + [(1/10) * (Constants.screen_width) + k * ((Constants.screen_width * 3/4) / 5) + (20*k) for k in range(5)] + [(1/10) * (Constants.screen_width) + k * ((Constants.screen_width * 3/4) / 5) + (20*k) for k in range(5)]
        self.square_ypositions = [(1/10) * Constants.screen_height + 90 * (k // 5) for k in range(len(self.square_xpositions))]
        self.squares_list = [Squares(self.square_xpositions[square], self.square_ypositions[square]) for square in range(len(self.square_xpositions))]
        for square in self.squares_list:
            square.draw_square(self.screen)
        
        self.letterlist = []
        self.current_line = 0

        self.word = choice(Words.FIVE_LETTER_WORDS)
        # TEST CASE
        self.word = 'hello'
        print(self.word)


    def handle_events(self): #Handles pygame events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    guessedword = ''.join(self.letterlist)
                    if guessedword in Words.FIVE_LETTER_WORDS:
                        self.compare_words(self.letterlist)
                        self.current_line += 1
                        self.letterlist = []
                        #if self.current_line == 5:
                        #    self.screen.blit(pg.image.load('textGameOver.png').convert_alpha(), (Constants.screen_width / 5, Constants.screen_height / 2))
                elif event.key == pg.K_BACKSPACE and len(self.letterlist) > 0:
                    self.letterlist.pop()
                    self.squares_list[len(self.letterlist) + self.current_line * 5].color_square(self.screen, [255, 255, 255])
                    
                else:
                    self.letterlist += event.unicode
                    for letter in range(len(self.letterlist)):
                        self.squares_list[letter + self.current_line * 5].add_text(self.screen, self.letterlist[letter].upper())
    
    def compare_words(self, guessedword):
        for letter in range(len(guessedword)):
            loc_in_letters = Constants.keys.index(guessedword[letter].upper())
            if guessedword[letter] == self.word[letter]:
                self.squares_list[letter + self.current_line * 5].color_square(self.screen, Constants.correct_color)
                self.keys_list[loc_in_letters].update_rect_color(self.screen, Constants.correct_color, guessedword[letter].upper())
            elif guessedword[letter] in self.word:
                self.squares_list[letter + self.current_line * 5].color_square(self.screen, Constants.inword_color)
                self.keys_list[loc_in_letters].update_rect_color(self.screen, Constants.inword_color, guessedword[letter].upper())
            else:
                self.squares_list[letter + self.current_line * 5].color_square(self.screen, Constants.missing_color)
                self.keys_list[loc_in_letters].update_rect_color(self.screen, Constants.missing_color, guessedword[letter].upper())
            self.squares_list[letter + self.current_line * 5].add_text(self.screen, guessedword[letter].upper())
        if ''.join(guessedword) == self.word:
            self.screen.blit(pg.image.load('textGameOver.png').convert_alpha(), (Constants.screen_width / 5, Constants.screen_height / 2))

            

        

    def update(self): #Checks word, updates everything
        pg.display.flip()