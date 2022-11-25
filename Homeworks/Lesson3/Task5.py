"""

Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. [Негафибоначчи]

Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

В математике, числа негафибоначчи — отрицательно индексированные элементы последовательности чисел Фибоначчи.
Числа негафибоначчи определяются индуктивно следующим рекуррентным соотношением:

F−1 = 1,
F−2 = -1,
Fn = F(n+2)−F(n+1).

"""


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def negafibonacci(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    return negafibonacci(n + 2) - negafibonacci(n + 1)


def input_values():
    correct_value = False
    while not correct_value:
        try:
            number = int(input("Введите число: "))
            correct_value = True
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return number


def calculate_values(n):
    lst: list[int] = []
    for i in range(n, 0, -1):
        lst.append(negafibonacci(-i))
    lst.append(0)
    for i in range(1, n + 1):
        lst.append(fibonacci(i))
    return lst


list_fibo: list[int] = calculate_values(input_values())
print(list_fibo)
