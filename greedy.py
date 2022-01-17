from multiprocessing.spawn import import_main_path


import chess


def greedy(board):
    """
    Greedy algorithm to find the best move.
    """
    legal_moves = board.legal_moves
    if len(legal_moves) == 0:
        return None

    best_move = legal_moves[0]
    best_score = board.is_checkmate()
    for move in legal_moves:
        board.push(move)
        score = board.is_checkmate()
        if score < best_score:
            best_move = move
            best_score = score
        board.pop()
    return best_move
