"""

3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.

"""


def my_func(arg1, arg2, arg3):
    if arg1 >= arg2 >= arg3:
        return arg1 + arg2
    elif arg1 >= arg3 >= arg2:
        return arg1 + arg3
    else:
        return arg2 + arg3


result = my_func(int(input("Введите первое число: ")),
                 int(input("Введите второе число: ")),
                 int(input("Введите третье число: ")))
print(f"Результат = {result}")
