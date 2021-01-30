""" 
The old classic tic-tac-toe 

| X | O | X |
-------------
| O | O | X |
-------------
| O | X | O |

X-Player : playes with X, O-Player : chooses O

"""

import random
import math
from moves import all_moves

class Player:
    def __init__(self, choice_letter):
        # Choice letter X or O
        self.choice = choice_letter
    
    # Returns the move for Player and the Computer(random) 
    def get_move(self):
        pass


class ComputerPlayer(Player):

    def __init__(self,choice):
        super().__init__(choice)
    
    # Picking moves is random for now
    def get_move(self, game):

        # Random choice for the computer
        move = random.choice(game.check_spaces())
        return move

class SmartComputerPlayer(Player):
    
    def __init__(self,choice):
        super().__init__(choice)

    def get_move(self,game):
        # Check if the board is empty and it's the bot's turn (in case if 2 bots are playing againest each other)
        if game.get_empty_places()[1] == len(game.board)**2:
            # Random choice
            played_spot = random.choice(game.check_spaces())
        else:
            # Getting the best move,, better implementation is to sep minmax and bestMove to diff methods
            played_spot = self.minmax(game, self.choice)['pos']

        return played_spot

    def minmax(self, game, choice_letter):

        # Who's to maxmize for ?
        maximize = self.choice

        # Checking the opponent player (in case of flipping the players 2 bots competing)
        other_maxmin = 'X' if choice_letter =='O' else 'O'

        # Base cases ,,, checking if there is already a winner
        if game.winner == other_maxmin:
            return {
                'pos': (None,None),
                'score' : 1*(game.get_empty_places()[1] + 1) if other_maxmin == maximize else -1*(game.get_empty_places()[1] + 1) # According to the minMax algo
            }
        # No empty spots
        # None won
        elif not game.get_empty_places()[0]:
            return {
                'pos' : (None,None),
                'score' : 0
            }
        
        ## The algo here ##
        # Check if the player is max player(the one that should win)
        if choice_letter == maximize:
            best = {'pos': (None,None), 'score': -math.inf } # Lowest score since we're going to maximize it 
        else:
            best = {'pos': (None,None), 'score': math.inf } # Highest score since we're going to minimize it 

        # Checking for every spot available to play
        # check_spaces returns tuple of position (x,y)
        for x,y in game.check_spaces():
            # 1 Making a move 
            game.make_move((x,y), choice_letter)

            # 2 what happens after that move , using recursion to get all the move
            score  = self.minmax(game, other_maxmin)

            # 3 unmake that move so it's not written over the board and let the bot continue trying other moves 
            game.board[x][y] = ' '
            game.winner = None
            score['pos'] = (x,y)

            # # 4 updating the score and pos 
            # if choice_letter == maximize:
            #     best = max(score['score'], best['score'])
            # else:
            #     best = min(score['score'], best['score'])
            
            if choice_letter == maximize:  # X is max player
                if score['score'] > best['score']:
                    best = score
            else:
                if score['score'] < best['score']:
                    best = score

        return best


class RealPlayer(Player):

    def __init__(self,choice):
        super().__init__(choice)
    
    # Player chooses the move
    def get_move(self, game):
        move = None
        is_valid_move = False

        while not is_valid_move:
            # Getting input from user
            spot = input("Enter a move from (0-8): ")
            
            try:
                move = int(spot)
                # Crazy shit here
                
                move = all_moves[move]
                if move not in game.check_spaces():
                    raise ValueError("Doesn't exist")
                
                is_valid_move = True
            except ValueError:
                print("Choose a valid move")
        return move