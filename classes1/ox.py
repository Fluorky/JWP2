class TicTacToe:
    ALL_SPACES = list('123456789')
    X, O, BLANK = 'X', 'O', ' '

    def __init__(self):
        self.board = self.get_blank_board()
        self.current_player = self.X

    def get_blank_board(self):
        board = {}
        for space in self.ALL_SPACES:
            board[space] = self.BLANK
        return board

    def get_board_str(self):
        return f'''
                {self.board['1']}|{self.board['2']}|{self.board['3']} 1 2 3 
                -+-+-
                {self.board['4']}|{self.board['5']}|{self.board['6']} 4 5 6 
                -+-+-
                {self.board['7']}|{self.board['8']}|{self.board['9']} 7 8 9'''

    def is_valid_space(self, space):
        if space is None:
            return False
        return space in self.ALL_SPACES and self.board[space] == self.BLANK

    def is_winner(self, player):
        b = self.board
        p = player
        return ((b['1'] == b['2'] == b['3'] == p) or
                (b['4'] == b['5'] == b['6'] == p) or
                (b['7'] == b['8'] == b['9'] == p) or
                (b['1'] == b['4'] == b['7'] == p) or
                (b['2'] == b['5'] == b['8'] == p) or
                (b['3'] == b['6'] == b['9'] == p) or
                (b['3'] == b['5'] == b['7'] == p) or
                (b['1'] == b['5'] == b['9'] == p))

    def is_board_full(self):
        for space in self.ALL_SPACES:
            if self.board[space] == self.BLANK:
                return False
        return True

    def update_board(self, space, mark):
        self.board[space] = mark

    def play_game(self):
        print('Welcome to Tic-Tac-Toe!')
        while True:
            print(self.get_board_str())
            move = None
            while not self.is_valid_space(move):
                print(f"What's {self.current_player}'s move? (1-9)")
                move = input()
            self.update_board(move, self.current_player)
            if self.is_winner(self.current_player):
                print(self.get_board_str())
                print(f'{self.current_player} wins!')
                break
            elif self.is_board_full():
                print(self.get_board_str())
                print('The game is a tie!')
                break
            self.current_player = self.O if self.current_player == self.X else self.X
        print('Thanks for playing!')


if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
