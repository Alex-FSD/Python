"""

5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

"""

with open("task5.txt", "w", encoding="utf-8") as my_f:
    line = input("Введите числа через пробел: ")
    my_f.writelines(line)
with open("task5.txt", "r", encoding="utf-8") as my_f:
    line = my_f.read().split()
    result = 0
    for i in line:
        result += int(i)
    print(f"Сумма = {result}")
