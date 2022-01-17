import chess
from greedy import Greedy


class State:
    def __init__(self):
        self.board = chess.Board()

    def new_game(self):
        self.board.reset()

    def get_legal_moves(self):
        return self.board.legal_moves

    def make_move(self, move):
        self.board.push(move)

    def undo_last_move(self):
        return self.board.pop()

    def get_score(self):
        pass

    def get_next_move(self):
        greedy_strategy = Greedy(self.board, self.board.turn)
        move = greedy_strategy.greedy()
        print(move)

    def get_board(self):
        return self.board


s = State()
print(s.get_next_move())
