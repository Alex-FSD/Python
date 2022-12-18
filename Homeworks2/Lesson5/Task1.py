"""

1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.

"""

with open("task1.txt", "w", encoding="utf-8") as my_f:
    while True:
        line = input("Введите текст: ")
        if not line:
            break
        my_f.write(line + "\n")

with open("task1.txt", "r", encoding="utf-8") as my_f:
    line = my_f.read()
    print(line)
