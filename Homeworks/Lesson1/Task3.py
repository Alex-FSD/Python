"""

Напишите программу, которая принимает на вход координаты точки (X и Y),
причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3

"""


def input_values():
    xy = ["X", "Y"]
    a = [0.0, 0.0]
    for i in range(2):
        correct_value = False
        while not correct_value:
            try:
                a[i] = float(input(f"Введите {xy[i]}: "))
                correct_value = True
                if a[i] == 0:
                    correct_value = False
                    print("Ошибка: Координаты X и Y не должны быть равными 0 ")
            except ValueError:
                print("Ошибка: Введено не корректное значение")
    return a


def calculate_values(xy):
    if xy[0] > 0 and xy[1] > 0:
        quarter = 1
    elif xy[0] < 0 and xy[1] > 0:
        quarter = 2
    elif xy[0] < 0 and xy[1] < 0:
        quarter = 3
    elif xy[0] > 0 and xy[1] < 0:
        quarter = 4
    print(f"Точка находится в {quarter} четверти плоскости")


calculate_values(input_values())
