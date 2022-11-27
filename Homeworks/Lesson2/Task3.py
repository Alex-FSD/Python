"""

Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

(1+1/n)^n

Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

PS - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.49, 2.52]

"""

try:
    n: int = int(input("Введите число n: "))
except ValueError:
    print("Ошибка: Введено не корректное значение")
    exit(1)

sequences: list[float] = [round((1 + 1 / i) ** i, 2) for i in range(1, n + 1)]
print(f"Список: {sequences}")
print(f"Сумма = {round(sum(sequences), 2)}")
