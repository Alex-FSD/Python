"""

Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

"""

from math import pi


def input_values():
    correct_value = False
    while not correct_value:
        try:
            number = int(input("Введите точность числа Пи: "))
            correct_value = True
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return number


d = input_values()
print(f'Число Пи = {round(pi, d)}')
