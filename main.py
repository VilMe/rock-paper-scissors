import sys
import random


class RPS:          #creating a class because we need to define some state
    def __init__(self):
        print('Welcome to Rock Paper Scissor - VilmaNation Style')
        
        self.moves: dict ={'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}

        self.valid_moves: list[str] = list(self.moves.keys())


        self.user_score: int = 0
        self.ai_score: int = 0   
    def play_game(self):
        user_move: str = input('Rock, paper, or scissors? >>').lower() 


        if user_move == 'exit':
            print('Thanks for playing, playa, lates!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid move...')
            return self.play_game()
        
        ai_move: str = random.choice(self.valid_moves)


        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)
        

    def display_moves(self, user_move: str, ai_move: str):
        print('-----') # divider to show when user inputs move
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[ai_move]}')
        print('-----')

    def check_move(self, user_move: str, ai_move: str):


        if user_move == ai_move:
            print('It\'s a tie! Play again??')
            print(f'Human score: {self.user_score}')
            print(f'Machines score: {self.ai_score}')
        elif user_move == 'rock' and ai_move == 'scissors':
            self.user_score += 1
            print('You win! one for the huamans!')
            print(f'Human score: {self.user_score}')
            print(f'Machines score: {self.ai_score}')
        elif user_move == 'scissors' and ai_move == 'paper':
            self.user_score += 1
            print('You win! one for the huamans!')
            print(f'Human score: {self.user_score}')
            print(f'Machines score: {self.ai_score}')
        elif user_move == 'paper' and ai_move == 'rock':
            self.user_score += 1
            print('You win! one for the huamans!')
            print(f'Human score: {self.user_score}')
            print(f'Machines score: {self.ai_score}')
        else: 
            self.ai_score += 1
            print('AI wins...the machines are taking over, I\'ve seen this movie before! RUN!')
            print(f'Human score: {self.user_score}')
            print(f'Machines score: {self.ai_score}')




if __name__ == '__main__':
    rps = RPS()

    while True:
        rps.play_game()