from multiprocessing.spawn import import_main_path


import chess
from collections import defaultdict
from scores import PIECE_SCORE_MAP, PIECES


class Greedy:
    def __init__(self, board, curr_color, depth_level=2) -> None:
        self.board = board
        self.curr_color = curr_color
        self.opp_color = not curr_color  # chess.WHITE is True and chess.BLACK is False
        self.SCORES = [None, None]  # (white_score, black_score)
        self.depth_level = depth_level
        self.CHECKMATE_SCORE = 99999

    # computes score of a given color for a given board
    def compute_score(self):
        if self.board.is_checkmate():
            return self.CHECKMATE_SCORE

        for i, color in enumerate([chess.WHITE, chess.BLACK]):
            score = 0
            for piece in PIECES:
                score += PIECE_SCORE_MAP[piece] * \
                    len(self.board.pieces(piece, color))

            self.SCORES[i] = score

        return {chess.WHITE: self.SCORES[0], chess.BLACK: self.SCORES[1]}

    def greedy(self):
        """
        Greedy algorithm to find the best move.
        """
        curr_legal_moves = self.board.legal_moves

        best_move = None
        best_score_diff = 0

        print(self.compute_score())
        for curr_move in curr_legal_moves:
            self.board.push(curr_move)
            opposing_legal_moves = self.board.legal_moves

            for opp_move in opposing_legal_moves:

                self.board.push(opp_move)

                # score after making two moves
                score_diff = abs(self.compute_score()[
                                 chess.WHITE] - self.compute_score()[chess.BLACK])

                if score_diff > best_score_diff:
                    score_diff = best_score_diff
                    best_move = curr_move
                self.board.pop()

            self.board.pop()

        return best_move
