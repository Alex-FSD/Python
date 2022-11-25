"""

Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""

"""

from random import randint


def input_values(name):
    correct_value = False
    while not correct_value:
        try:
            x = int(input(f"Ходит {name}: "))
            if x < 1 or x > 28:
                print("Ошибка: Значение должно быть от 1 до 28")
            else:
                correct_value = True
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return x


def game_score(name, c_move, counter, c_count):
    print(f"{name}, взял {c_move}, теперь у него {counter} конфет.")
    print(f"На столе осталось {c_count} конфет.")
    print()


candy_count = 2021
player1 = "Игрок1"
player2 = "Игрок2"
counter1 = 0
counter2 = 0

print(f"На столе лежит {candy_count} конфета. Играют \"{player1}\" и \"{player2}\" делая ход друг после друга.")
print(f"Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.")
print(f"Все конфеты оппонента достаются сделавшему последний ход.")
print(f"Цель: забрать все конфеты у своего конкурента")
print()

token = randint(0, 2)
if token:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

while candy_count > 28:
    if token:
        candy_move = input_values(player1)
        counter1 += candy_move
        candy_count -= candy_move
        token = False
        game_score(player1, candy_move, counter1, candy_count)
    else:
        candy_move = input_values(player2)
        counter2 += candy_move
        candy_count -= candy_move
        token = True
        game_score(player2, candy_move, counter2, candy_count)

if token:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
