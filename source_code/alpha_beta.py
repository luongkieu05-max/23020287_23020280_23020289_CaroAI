# ===============================
# File: alpha_beta.py
# Chức năng:
# - Cài đặt thuật toán Alpha-Beta Pruning
# - Dùng cùng hàm đánh giá với Minimax
# - Chọn nước đi tốt nhất cho AI
# ===============================

import math
import time

from board import BOARD_SIZE, EMPTY, PLAYER, AI, is_board_full
from game_rules import check_winner
from evaluation import evaluate


def alpha_beta(board, depth, maximizing, alpha, beta):
    """
    Thuật toán Alpha-Beta Pruning.
    """
    if check_winner(board, AI):
        return 1000

    if check_winner(board, PLAYER):
        return -1000

    if is_board_full(board):
        return 0

    if depth == 0:
        return evaluate(board)

    if maximizing:
        best = -math.inf

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = AI

                    score = alpha_beta(board, depth - 1, False, alpha, beta)

                    board[row][col] = EMPTY

                    best = max(best, score)
                    alpha = max(alpha, best)

                    if beta <= alpha:
                        return best

        return best

    best = math.inf

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER

                score = alpha_beta(board, depth - 1, True, alpha, beta)

                board[row][col] = EMPTY

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    return best

    return best


def best_move_alpha_beta(board, depth=3):
    """
    Chọn nước đi tốt nhất cho AI bằng Alpha-Beta Pruning.
    """
    best_score = -math.inf
    move = None

    start = time.time()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = AI

                score = alpha_beta(
                    board,
                    depth - 1,
                    False,
                    -math.inf,
                    math.inf
                )

                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    move = (row, col)

    end = time.time()
    print("Thoi gian Alpha-Beta:", end - start)
    print("Nuoc di tot nhat:", move, "diem:", best_score)

    return move
