"""

Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.

"""


def input_int_values(text):
    number: int = 0
    correct_value = False
    while not correct_value:
        try:
            number = int(input(text))
            correct_value = True
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return number


def calculate_values(n):
    i = 2
    list_simple = []
    while i <= n:
        if n % i == 0:
            list_simple.append(i)
            n //= i
            i = 2
        else:
            i += 1
    return list_simple


num: int = input_int_values("Введите натуральное число: ")
print(f'Список простых множителей для {num} = {calculate_values(num)}')
