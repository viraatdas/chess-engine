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

    # compute the score based on a formula and current score
    def score_formula(self, white_score, black_score):
        pass

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

        curr_score = self.compute_score()[self.curr_color]
        opp_score = self.compute_score()[self.opp_color]

        # we want to maximize best_score_diff
        best_move = None
        best_score_diff = curr_score - opp_score

        for curr_move in curr_legal_moves:
            self.board.push(curr_move)
            opposing_legal_moves = self.board.legal_moves

            for opp_move in opposing_legal_moves:
                self.board.push(opp_move)
                curr_next_legal_moves = self.board.legal_moves
                for curr_next_move in curr_next_legal_moves:
                    self.board.push(curr_next_move)
                    # score after making two moves
                    opp_score_after_two_moves = self.compute_score()[
                        self.opp_color]
                    curr_score_after_two_moves = self.compute_score()[
                        self.curr_color]

                    score_diff = curr_score_after_two_moves - opp_score_after_two_moves
                    if score_diff > best_score_diff:
                        best_score_diff = score_diff
                        best_move = curr_move

                    self.board.pop()
                self.board.pop()
            self.board.pop()

        return best_move
