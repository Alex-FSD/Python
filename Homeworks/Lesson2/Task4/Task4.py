"""

Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.

"""

import random

file_name: str = "file.txt"


def file_write(number):
    with open(file_name, "w") as data:
        for i in range(number):
            data.write(f"{random.randrange(0, 2 * number)}\n")


def file_read():
    with open(file_name, "r") as data:
        indexs: list[int] = list(map(int, data.readlines()))
    return indexs


n = int(input("Введите число N: "))
list_number = [i for i in range(-n, n + 1)]
file_write(n)
list_index = file_read()

print()
print(f"Список чисел = {list_number}")
print(f"Список индексов = {list_index}")

result: int = 1
expression: str = ""
for i in range(len(list_index)):
    result *= list_number[list_index[i]]
    expression += f"{list_number[list_index[i]]}"
    if i != len(list_index) - 1:
        expression += " * "

print()
print(f"{expression} = {result}")
