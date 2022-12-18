"""

3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32

"""
import random

lst = []
for i in range(1, 11):
    lst.append(["Сотрудник" + str(i), str(random.randrange(5000, 30000) + round(random.random(), 2))])
with open("task3.txt", "w", encoding="utf-8") as my_f:
    for i in lst:
        my_f.write(i[0] + " " + i[1] + "\n")

with open("task3.txt", "r", encoding="utf-8") as my_f:
    lst = []
    sum_salary = 0.0
    line = my_f.readlines()
    for i in line:
        lst.append(i.split())
    for i in range(len(lst)):
        sum_salary += float(lst[i][1])
        if float(lst[i][1]) < 20000:
            print(f"{lst[i][0]} {lst[i][1]}")
    print()
    print(f"Средний доход сотрудников = {sum_salary / len(lst):.2f}")
