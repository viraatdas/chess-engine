from multiprocessing.spawn import import_main_path


import chess
from collections import defaultdict
from constants import PIECE_SCORE_MAP, PIECES


class Greedy:
    def __init__(self, board, curr_color, depth_level=2) -> None:
        self.board = board
        self.curr_color = curr_color
        self.opp_color = not curr_color  # chess.WHITE is True and chess.BLACK is False

        self.depth_level = depth_level
        self.CHECKMATE_SCORE = 99999

    # computes score of a given color for a given board
    def compute_score(self) -> dict:
        # ex of map: {chess.WHITE: 0, chess.BLACK: 0}
        SCORES = defaultdict(lambda: 0)
        if self.board.is_checkmate():
            SCORES[self.curr_color] = self.CHECKMATE_SCORE
            return SCORES

        for color in [chess.WHITE, chess.BLACK]:
            score = 0
            for piece in PIECES:
                score += PIECE_SCORE_MAP[piece] * \
                    len(self.board.pieces(piece, color))

            SCORES[color] = score

        return SCORES

    def compute_score_for_curr_color(self):
        return self.compute_score()[self.curr_color]

    def greedy(self):
        """
        Greedy algorithm to find the best move.
        """
        curr_legal_moves = self.board.legal_moves

        white_score, black_score = self.compute_score()

        best_move = None
        best_score_diff = -1

        for curr_move in curr_legal_moves:
            self.board.push(curr_move)
            opposing_legal_moves = self.board.legal_moves

            for opp_move in opposing_legal_moves:
                self.board.push(opp_move)

                # score after making two moves
                if self.curr_color == chess.WHITE:
                    _, curr_black_score = self.compute_score()
                    curr_score_diff = black_score - curr_black_score

                else:
                    curr_white_score, _ = self.compute_score()
                    curr_score_diff = white_score - curr_white_score

                if curr_score_diff > best_score_diff:
                    best_score_diff = curr_score_diff
                    best_move = curr_move

                self.board.pop()

            self.board.pop()

        return best_move
