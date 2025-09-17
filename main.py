import sys
import random


class RPS:          #creating a class because we need to define some state
    def __init__(self):
        print('Welcome to Rock Paper Scissor - VilmaNation Style')
        
        self.moves: dict ={'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}