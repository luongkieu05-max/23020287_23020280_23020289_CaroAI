# ===============================
# File: main.py
# Chức năng:
# - File chạy chính của chương trình
# - Chọn chế độ AI (Minimax / Alpha-Beta)
# - Khởi động giao diện pygame
# ===============================

from ui_pygame import main as run_pygame


def choose_ai_mode():
    """
    Cho người dùng chọn chế độ AI trước khi mở pygame.
    1: Minimax
    2: Alpha-Beta Pruning
    """
    while True:
        print("===== CHON CHE DO AI =====")
        print("1. Minimax")
        print("2. Alpha-Beta Pruning")

        choice = input("Nhap lua chon cua ban: ")

        if choice == "1":
            print("Ban da chon che do Minimax")
            return "MINIMAX"

        if choice == "2":
            print("Ban da chon che do Alpha-Beta Pruning")
            return "ALPHA_BETA"

        print("Lua chon khong hop le. Vui long nhap lai.")


if __name__ == "__main__":
    ai_mode = choose_ai_mode()
    run_pygame(ai_mode)
