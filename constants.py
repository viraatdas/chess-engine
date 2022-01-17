import chess

PIECE_SCORE_MAP = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3,
                   chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 0}

PIECES = PIECE_SCORE_MAP.keys()

VALID_COLOR_LIST = ["white", "black"]
