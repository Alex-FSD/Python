"""

Создайте программу для игры в ""Крестики-нолики"".

"""
import random


def print_board(board):
    for i in range(3):
        b1: str = board[0 + i * 3]
        b2: str = board[1 + i * 3]
        b3: str = board[2 + i * 3]
        if b1 == "X":
            b1 = "\033[1m" + "\033[31m" + "X" + "\033[0m"
        elif b1 == "O":
            b1 = "\033[1m" + "\033[33m" + "O" + "\033[0m"
        if b2 == "X":
            b2 = "\033[1m" + "\033[31m" + "X" + "\033[0m"
        elif b2 == "O":
            b2 = "\033[1m" + "\033[33m" + "O" + "\033[0m"
        if b3 == "X":
            b3 = "\033[1m" + "\033[31m" + "X" + "\033[0m"
        elif b3 == "O":
            b3 = "\033[1m" + "\033[33m" + "O" + "\033[0m"
        print("|", b1, "|", b2, "|", b3, "|")


def check_winner(board):
    winning_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in winning_combo:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False


def input_values(token, board):
    valid = False
    while not valid:
        player = input("Ваш ход: ")
        try:
            player = int(player)
        except ValueError:
            print("Ошибка: Введенное значение не является числом.")
            continue
        if player >= 1 and player <= 9:
            if (str(board[player - 1]) not in "XO"):
                board[player - 1] = token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Ошибка: Введите число от 1 до 9.")


def random_values(token, board):
    valid = False
    while not valid:
        bot = random.randint(1, 9)
        if (str(board[bot - 1]) not in "XO"):
            board[bot - 1] = token
            valid = True


board = list(range(1, 10))
counter = 0
win = False
print("Начало игры:")
while not win:
    print_board(board)
    if counter % 2 == 0:
        input_values("X", board)
    else:
        print("Ход компьютера: ")
        random_values("O", board)
    counter += 1
    if counter > 4:
        tmp = check_winner(board)
        if tmp:
            print_board(board)
            print()
            print("\033[1m" + "\033[32m" + f"{tmp} Выиграл!" + "\033[0m")
            win = True
            break
    if counter == 9:
        print_board(board)
        print()
        print("\033[1m" + "\033[32m" + "Ничья!" + "\033[0m")
        break
