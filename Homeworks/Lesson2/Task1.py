"""

Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11

"""


def input_values(inputText):
    correct_value = False
    while not correct_value:
        try:
            number = float(input(f"{inputText}"))
            correct_value = True
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return number


def calculate_values(num):
    sum = 0
    for i in str(num):
        if i != "." and i != "-":
            sum += int(i)
    return sum


num = input_values("Введите число: ")

print(f"Сумма цифр = {calculate_values(num)}")
