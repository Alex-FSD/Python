"""

Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

"""


def input_values(inputText):
    correct_value = False
    while not correct_value:
        try:
            number = int(input(f"{inputText}"))
            correct_value = True
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return number


def calculate_values(n):
    if n == 1:
        return 1
    else:
        return n * calculate_values(n - 1)


num = input_values("Введите число: ")

list = []
for i in range(1, num + 1):
    list.append(calculate_values(i))

print(f"Произведения чисел от 1 до {num}:  {list}")
