# ===============================
# File: main.py
# Chức năng:
# - File chạy chính của chương trình
# - Menu console: chọn chế độ AI, chơi pygame, chơi lại hoặc thoát
# ===============================

from ui_pygame import main as run_pygame


def show_menu():
    """In menu chọn chế độ trên console."""
    print()
    print("===== CARO AI =====")
    print("1. Minimax")
    print("2. Alpha-Beta Pruning")
    print("0. Thoat chuong trinh")
    print()


def choose_ai_mode():
    """
    Cho người dùng chọn chế độ AI trên console.
    Trả về "MINIMAX", "ALPHA_BETA" hoặc None nếu chọn thoát.
    """
    while True:
        show_menu()
        choice = input("Nhap lua chon cua ban: ").strip()

        if choice == "0":
            return None

        if choice == "1":
            print("Ban da chon che do Minimax")
            return "MINIMAX"

        if choice == "2":
            print("Ban da chon che do Alpha-Beta Pruning")
            return "ALPHA_BETA"

        print("Lua chon khong hop le. Vui long nhap lai.")


if __name__ == "__main__":
    while True:
        ai_mode = choose_ai_mode()

        if ai_mode is None:
            print("Tam biet!")
            break

        run_pygame(ai_mode)

        print()
        print("Van choi da ket thuc. Ban co the chon che do moi.")
