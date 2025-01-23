# Adrianna Barrera
# Tic Tac Toe AI Project1
# Game logic and main
import math
import time
from player import MM_Alpha_Beta, MiniMax_Player


class TicTacToe():
    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None

    # Creates the board
    @staticmethod
    def create_board():
        return [' ' for _ in range(9)]


    def display_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # checks rows
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, x_wins, o_wins, draws, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    x_total_time = 0
    o_total_time = 0
    num_moves = 0

    while game.empty_squares():
        start_time = time.time()  # Start timing the move
        if letter == 'O':
            square = o_player.get_move(game)
            o_total_time += time.time() - start_time
        else:
            square = x_player.get_move(game)
            x_total_time += time.time() - start_time
        num_moves += 1

        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square+1))
                game.display_board()
                print('')

            if game.current_winner:
                if game.current_winner == 'X':
                    x_wins += 1
                elif game.current_winner == 'O':
                    o_wins += 1
                else:
                    draws += 1

                if print_game:
                    print(letter + ' wins!')
                    print("\nX wins: " + str(x_wins))
                    print("\nO wins: " + str(o_wins))
                    print("\nDraws: " + str(draws))
                return game.current_winner  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.0001)

    if print_game:
        print('It\'s a tie!')
        draws += 1

    return 'draw', x_total_time / num_moves, o_total_time / num_moves  # Return 'draw' if no winner


if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    draws = 0
    num_games = 100  # Number of games to play
    x_total_avg_time = 0
    o_total_avg_time = 0

    for game_num in range(1, num_games + 1):
        print("Game #" + str(game_num))
        x_player = MiniMax_Player('X')
        o_player = MM_Alpha_Beta('O')
        t = TicTacToe()
        winner, x_avg_time, o_avg_time = play(t, x_player, o_player, x_wins, o_wins, draws, print_game=True)
        if winner == 'X':
            x_wins += 1
        elif winner == 'O':
            o_wins += 1
        else:
            draws += 1
        x_total_avg_time += x_avg_time
        o_total_avg_time += o_avg_time

    x_total_avg_time /= num_games
    o_total_avg_time /= num_games

    print("\nFinal Results:")
    print("X wins:", x_wins)
    print("O wins:", o_wins)
    print("Draws:", draws)
    print("Average time taken for X's moves:", (x_total_avg_time * 100))
    print("Average time taken for O's moves:", (o_total_avg_time * 100))

