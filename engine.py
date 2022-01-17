import chess
from greedy import Greedy


class Engine:
    def __init__(self):
        self.board = chess.Board()

    def new_game(self):
        self.board.reset()

    def get_legal_moves(self):
        return self.board.legal_moves

    def make_move(self, move):
        self.board.push(move)

    def input_make_move(self, input_move):
        try:
            move = self.board.parse_san(input_move)
            self.make_move(move)
            return True
        except ValueError:
            return False

    def undo_last_move(self):
        return self.board.pop()

    def get_next_move(self):
        greedy_strategy = Greedy(self.board, self.board.turn)
        move = greedy_strategy.greedy()
        return move

    def make_next_move(self):
        move = self.get_next_move()
        self.make_move(move)
        return move

    def print_board(self):
        print(self.board)

    def is_check(self):
        return self.board.is_check()

    def is_checkmate(self):
        return self.board.is_checkmate()

    def is_stalemate(self):
        return self.board.is_stalemate()
