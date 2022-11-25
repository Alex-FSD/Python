"""

Задана натуральная степень k.
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
и записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

"""

import random


def input_int_values(text):
    number: int = 0
    correct_value = False
    while not correct_value:
        try:
            number = int(input(text))
            if number > 0:
                correct_value = True
            else:
                print("Ошибка: Введено не натуральное число")
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return number


def calculate_values(lst):
    s: str = ""
    for i in range(len(lst)):
        if i < len(lst) - 2:
            if lst[i] > 1:
                s += f"{lst[i]}x^{len(lst) - i - 1}"
            elif lst[i] == 1:
                s += f"x^{len(lst) - i - 1}"
            if lst[i + 1] != 0:
                s += " + "
        elif i == len(lst) - 2:
            if lst[i] > 1:
                s += f"{lst[i]}x"
            elif lst[i] == 1:
                s += f"x"
            if lst[i + 1] != 0:
                s += " + "
        elif i == len(lst) - 1:
            if lst[i] >= 1:
                s += f"{lst[i]}"
    s += " = 0"
    print(s)
    return s


def file_write(s):
    with open("file.txt", "w") as data:
        data.write(s)


k: int = input_int_values("Введите натуральную степень k = ")
list_coefficients = [random.randint(0, 100) for i in range(k + 1)]
file_write(calculate_values(list_coefficients))
