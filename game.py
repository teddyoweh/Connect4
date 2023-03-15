import numpy as np
import os

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((10, 10), dtype=int)
    
    def check_win(self):
        for row in range(10):
            for col in range(7):
                if self.board[row][col] == self.board[row][col+1] == self.board[row][col+2] == self.board[row][col+3] != 0:
                    return self.board[row][col]
        for row in range(7):
            for col in range(10):
                if self.board[row][col] == self.board[row+1][col] == self.board[row+2][col] == self.board[row+3][col] != 0:
                    return self.board[row][col]
        for row in range(7):
            for col in range(7):
                if self.board[row][col] == self.board[row+1][col+1] == self.board[row+2][col+2] == self.board[row+3][col+3] != 0:
                    return self.board[row][col]
        for row in range(3, 10):
            for col in range(7):
                if self.board[row][col] == self.board[row-1][col+1] == self.board[row-2][col+2] == self.board[row-3][col+3] != 0:
                    return self.board[row][col]
        return None
    
    def check_free(self, col):
        start = 9
        while self.board[start][col]!=0:
            start -= 1
            if start<0:
                return None
        return start
    
    def print_board(self):
        for row in self.board:
            print(" | ".join(str(cell) for cell in row))
            print('')
    
    def print_game(self):
        print('\n')
        self.print_board()
        print('*'*38)
        print('')
        print(" | ".join([str(i+1) for i in range(10)]))
        print('\n')
        
    def play_game(self):
        while True:
            self.print_game()
            user_input = input('Player 1: > ')
            try:
                user_input = int(user_input)
            except:
                print("Please enter a number")
            else:
                if user_input > 10 or user_input < 1:
                    print("Please enter a number between 1 and 10")
                else:
                    col = user_input - 1
                    row = self.check_free(col)
                    if row is None:
                        print("Column is full. Try again.")
                    else:
                        self.board[row][col] = 1
                        
            os.system('clear')
            self.print_game()

            winner = self.check_win()
            if winner:
                print("Player {} wins!".format(winner))
                break
            
            ex_input = input('Player 2: > ')
            try:
                ex_input = int(ex_input)
            except:
                print("Please enter a number")
            else:
                if ex_input > 10 or ex_input < 1:
                    print("Please enter a number between 1 and 10")
                else:
                    col = ex_input - 1
                    row = self.check_free(col)
                    if row is None:
                        print("Column is full. Try again.")
                    else:
                        self.board[row][col] = 2
              
            os.system('clear')



if __name__ == '__main__':
    game = ConnectFour()
    game.play_game()
