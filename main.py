import sys
import random


class RPS:          #creating a class because we need to define some state
    def __init__(self):
        print('Welcome to Rock Paper Scissor - VilmaNation Style')
        
        self.moves: dict ={'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}

        self.valid_moves: list[str] = list(self.moves.keys())


    def play_game(self):
        ...

    def display_move(self):
        ...

    def check_move(self):
        ...