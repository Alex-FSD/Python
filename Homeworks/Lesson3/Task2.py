"""

Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

"""
from math import ceil


def calculate_values(lst):
    new_list = [lst[i] * lst[len(lst) - i - 1] for i in range(ceil(len(lst) / 2))]
    return new_list


list_simple = [2, 3, 4, 5, 6]
print(f"{list_simple} => {calculate_values(list_simple)}")
list_simple = [2, 3, 5, 6]
print(f"{list_simple} => {calculate_values(list_simple)}")
