import random


class TictacToe:
    def __init__(self):
        self.board = []
        
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('_')
            self.board.append(row)
            
    def get_rand_player_one(self):
        return random.randint(0, 1)
    
    def fix_point(self, row, col, player):
        self.board[row][col] = player
        
    def player_won(self, player):
        n = len(self.board)
        board_values = set()
        
        # Check rows
        for i in range(n):
            for j in range(n):
                board_values.add(self.board[i][j])
            
            if board_values == {player}:
                return True
            else:
                board_values.clear()
            
        # Check for diagonals play
        for i in range(n):
            board_values.add(self.board[i][i])
        if board_values == {player}:
            return True
        else:
            board_values.clear()
            
        board_values.add(self.board[0][2])
        board_values.add(self.board[1][1])
        board_values.add(self.board[2][0])
        if board_values == {player}:
            return True
        else:
            return False
    
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '_':
                    return False
        return True
        
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print()
            
    def swap_player_turn(self, player):
        return 'O' if player == 'X' else 'X'
        
    def start(self):
        self.create_board()
        player = 'X' if self.get_rand_player_one() == 0 else 'O'
        game_over = False
        
        while not game_over:
            try:
                self.show_board()
                print(f'\nPlayer {player} turn')
                
                row, col = list(map(int, input("Enter row and column numbers to fix point: ").split()))
                
                print()
                
                if col is None:
                    raise ValueError("Not enough values to unpack (expected 2, got 1)")
                
                self.fix_point(row - 1, col - 1, player)
                    
                game_over = self.player_won(player)
                if game_over:
                    print(f'Player {player} wins the game!')
                    continue
                        
                game_over = self.is_board_filled()
                if game_over:
                    print("Its a Draw!")
                    continue
                        
                player = self.swap_player_turn(player)
                    
            except ValueError as err:
                print(err)
        
        print()
        self.show_board()
        
if __name__ == '__main__':
    tic_tac_toe = TictacToe()
    tic_tac_toe.start()



