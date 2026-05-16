# ===============================
# File: ai_minimax.py
# Chức năng:
# - Cài đặt thuật toán Minimax
# - Chọn nước đi tốt nhất cho AI
# ===============================

import math
import time

from board import BOARD_SIZE, EMPTY, PLAYER, AI, is_board_full
from game_rules import check_winner
from evaluation import evaluate


def minimax(board, depth, maximizing):
    """
    Thuật toán Minimax.
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
                    score = minimax(board, depth - 1, False)
                    board[row][col] = EMPTY
                    best = max(best, score)

        return best

    best = math.inf

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER
                score = minimax(board, depth - 1, True)
                board[row][col] = EMPTY
                best = min(best, score)

    return best


def best_move(board, depth=2):
    """
    Chọn nước đi tốt nhất cho AI bằng Minimax.
    """
    best_score = -math.inf
    move = None

    start = time.time()

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                score = minimax(board, depth - 1, False)
                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    move = (row, col)

    end = time.time()
    print("Thoi gian Minimax:", end - start)
    print("Nuoc di tot nhat:", move, "diem:", best_score)

    return move
