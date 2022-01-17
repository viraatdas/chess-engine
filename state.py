import chess


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

        pass

    def __get_board(self):
        return self.board
