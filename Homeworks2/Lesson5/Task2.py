"""

2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.

"""

lst = ["Test test test", "Test", "test test test test", "test test"]
with open("task2.txt", "w", encoding="utf-8") as my_f:
    for i in lst:
        my_f.write(i + "\n")

with open("task2.txt", "r", encoding="utf-8") as my_f:
    line = my_f.readlines()
    print(f"Количество строк в файле = {len(line)}")
    for i in range(len(line)):
        print(f"Количество слов в {i + 1} строке = {len(line[i].split())}")
