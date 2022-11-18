"""

Напишите программу, которая принимает на вход цифру,
обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет

"""


def input_values():
    global number
    correct_value: bool = False
    while not correct_value:
        try:
            number = int(input("Введите число от 1 до 7: "))
            correct_value = True
        except ValueError:
            print("Ошибка: Введенное значение не является числом.")
    return number


def calculate_values(num: int):
    if 6 <= num <= 7:
        print("Да")
    elif 1 <= num <= 5:
        print("Нет")
    else:
        print("Число вне пределов 7 дней")


calculate_values(input_values())
