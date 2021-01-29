class TicTacToe:
    def __init__(self):
    #    [[' ', ' ', ' '], 
    #     [' ', ' ', ' '], 
    #     [' ', ' ', ' ']]
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

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

