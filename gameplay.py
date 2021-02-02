from moves import all_moves
from player import RealPlayer, ComputerPlayer, SmartComputerPlayer

class TicTacToe:
    def __init__(self):
    #    [[' ', ' ', ' '], 
    #     [' ', ' ', ' '], 
    #     [' ', ' ', ' ']]
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None

    # Printing the board
    def print_board(self):

        print('-------------')
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    # Static method as it doesn't require self
    @staticmethod
    def map_board():
        mapped_board = [[str(i) for i in range(3*j, 3*(j+1))] for j in range(3) ]
        print('-------------')
        for row in mapped_board:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    # check for empty places/ available moves
    def check_spaces(self):
        empty_spaces = []
        for (j, row) in enumerate(self.board):
            for (i, place) in enumerate(row):
                if place == ' ':
                    empty_spaces.append((j, i))
        return empty_spaces
    
    def make_move(self, place, choice):
        # return True if the move is valid
        # [[0,1,2],[3,4,5],[6,7,8]]
        # Checking if the wanted place is empty

        row, col = place
        position = self.board[row][col]
        if position == ' ':
            self.board[row][col] = choice
            if self.win(place, choice):
                self.winner = choice
            return True
        return False 

    def get_empty_places(self):
        for row in self.board:
            for col in row:
                if col == ' ':
                    return True
        return False


    def num_empty_places(self):
        count = 0
        for row in self.board:
            for col in row:
                if col == ' ':
                    count += 1
        return count

    def win(self, place, choice):
        # Checking rows
        # print(place)
        rows = self.board[place[0]%3]
        if all(spot == choice for spot in rows):
            return True

        # Checking colums
        col_index = all_moves[place[1]][1]
        cols = [self.board[i][col_index] for i in range(3)]
        if all(spot == choice for spot in cols):
            return True

        # Checking the 2 diagonals
        # First diagonal from up right to down left
        d1 = [self.board[i][i] for i in range(3)]
        if all(spot == choice for spot in d1):
            return True

        d2 = [self.board[i][2-i] for i in range(3)]
        if all(spot == choice for spot in d2):
            return True

        return False
    
def play_loop(game, player_x, player_o, print_game=True):
    
    place = None
    if print_game:
        game.map_board()

    # We can going to play with X
    choice_letter = 'X'
    while game.get_empty_places():
        if choice_letter == 'O':
            place = player_o.get_move(game)
        else:
            place = player_x.get_move(game)
        
        if game.make_move(place, choice_letter):
            if print_game:
                print(f"{choice_letter}, moved to {place}")
                game.print_board()
                print()
            
            # Check the winner 
            if game.winner:
                if print_game:
                    print(choice_letter + ' Wins!!!')
                return choice_letter

            # Switching players
            choice_letter = 'X' if  choice_letter == 'O' else 'O'


    if print_game:
        print("Tie")


if __name__ == '__main__':
    player_x = RealPlayer('X')
    player_y = SmartComputerPlayer('O')
    # player_y = ComputerPlayer('O')
    game_ttt = TicTacToe()
    play_loop(game_ttt, player_x, player_y)


