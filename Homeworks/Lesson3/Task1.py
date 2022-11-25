"""

Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

"""


def calculate_values(lst):
    result: int = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            result += lst[i]
    return result


list_simple: list[int] = [2, 3, 5, 9, 3]
print(f"Список = {list_simple}")
print(f"Результат = {calculate_values(list_simple)}")
