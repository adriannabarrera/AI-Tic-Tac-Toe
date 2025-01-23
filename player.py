# Adrianna Barrera
# Tic Tac Toe AI Project1
# Minimax AI Player and Minimax Alpha-Beta Pruning player

import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def getMove(self, game):
        pass

class MM_Alpha_Beta(Player):
    def __init__(self, letter):
        self.letter = letter

    # Gets the square the AI choices
    def get_move(self, game):
        # If the square is empty
        if len(game.available_moves()) == 9:
            # Choose a random square
            square = random.choice(game.available_moves())
        else:
            # Else use the Minimax to determine the next best move
            square = self.minimax(game, self.letter, -math.inf, math.inf)['position']
        return square

    def minimax(self, state, player, alpha, beta):
        max_player = self.letter  # yourself
        # If your X then the other player is O and vice versa
        other_player = 'O' if player == 'X' else 'X'

        # Check if there is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                    state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player, alpha, beta)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # optimal next move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, best['score'])
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, best['score'])

            if alpha >= beta:
                break  # pruning

        return best


class MiniMax_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # optimal next move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
