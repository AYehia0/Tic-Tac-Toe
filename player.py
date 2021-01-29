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
from gameplay import TicTacToe

class Player:
    def __init__(self, choice_letter):
        # Choice letter X or O
        self.choice = choice_letter
    
    # Returns the move for Player and the Computer(random) 
    def get_move(self):
        pass


class ComputerPlayer(Player):

    def __init__(self,choice):
        super().__init__(self, choice)
    
    # Picking moves is random for now
    def get_move(self):

        # Random choice for the computer
        move = random.choice(TicTacToe.check_spaces())
        return move

class RealPlayer(Player):

    def __init__(self,choice):
        super().__init__(self, choice)
    
    # Player chooses the move
    def get_move(self):
        move = None
        is_valid_move = False

        while not is_valid_move:
            # Getting input from user
            spot = input("Enter a move from (0-8)")
            
            try:
                move = int(spot)
                # Crazy shit here
                c = {
                    0 : (0,0),
                    1 : (0,1),
                    2 : (0,2),
                    3 : (1,0),
                    4 : (1,1),
                    5 : (1,2),
                    6 : (2,0),
                    7 : (2,1),
                    8 : (2,2)
                }
                move = c[move]
                if move not in TicTacToe.check_spaces():
                    raise ValueError("Doesn't exist")
                
                is_valid_move = True
            except ValueError:
                print("Choose a valid move")
        return move