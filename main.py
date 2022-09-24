#Import modules
from game import Game

if __name__ == '__main__': #Checks if main file
    game = Game()

    while True: #Main game loop, runs functions from __init__.py
        game.handle_events()
        game.update()



