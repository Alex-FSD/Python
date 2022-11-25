"""

Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.

"""

import random


def input_int_values(text):
    number: int = 0
    correct_value = False
    while not correct_value:
        try:
            number = int(input(text))
            if number > 0:
                correct_value = True
            else:
                print("Ошибка: Введено не натуральное число")
        except ValueError:
            print("Ошибка: Введено не корректное значение")
    return number


def calculate_values(lst):
    s: str = ""
    for i in range(len(lst)):
        if i < len(lst) - 2:
            if lst[i] > 1:
                s += f"{lst[i]}x^{len(lst) - i - 1}"
            elif lst[i] == 1:
                s += f"x^{len(lst) - i - 1}"
            if lst[i + 1] != 0:
                s += " + "
        elif i == len(lst) - 2:
            if lst[i] > 1:
                s += f"{lst[i]}x"
            elif lst[i] == 1:
                s += f"x"
            if lst[i + 1] != 0:
                s += " + "
        elif i == len(lst) - 1:
            if lst[i] >= 1:
                s += f"{lst[i]}"
    s += " = 0"
    return s


def get_degree(d):
    if "x^" in d:
        i = d.find("^")
        num = int(d[i + 1:])
    elif ("x" in d) and ("^" not in d):
        num = 1
    else:
        num = -1
    return num


def get_coef(c):
    if "x" in c:
        i = c.find("x")
        if i != 0:
            num = int(c[:i])
        else:
            num = 1
    return num


def get_polynomial(s):
    s = s[0].replace(" ", "").split("=")
    s = s[0].split("+")
    lst = []
    lst_len = len(s)
    k = 0
    if get_degree(s[-1]) == -1:
        lst.append(int(s[-1]))
        lst_len -= 1
        k = 1
    i = 1
    j = lst_len - 1
    while j >= 0:
        if get_degree(s[j]) != -1 and get_degree(s[j]) == i:
            lst.append(get_coef(s[j]))
            j -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
    return lst


def parse_polynomial():
    lst1 = get_polynomial(list_from_file1)
    lst2 = get_polynomial(list_from_file2)
    lst_len = len(lst1)
    if len(lst1) > len(lst2):
        lst_len = len(lst2)
    lst_new = [lst1[i] + lst2[i] for i in range(lst_len)]
    if len(lst1) > len(lst2):
        for i in range(lst_len, len(lst1)):
            lst_new.append(lst1[i])
    else:
        for i in range(lst_len, len(lst2)):
            lst_new.append(lst2[i])
    lst_new.reverse()
    return lst_new


def file_write(name, s):
    with open(name, "w") as data:
        data.write(s)


def file_read(name):
    lst: list = []
    with open(name, "r") as data:
        lst = data.readlines()
    return lst


file1_name: str = "file1.txt"
file2_name: str = "file2.txt"
file_result_name: str = "file_result.txt"

k1: int = input_int_values("Введите натуральную степень для первого файла k = ")
k2: int = input_int_values("Введите натуральную степень для второго файла k = ")
list_coefficients1 = [random.randint(0, 100) for i in range(k1 + 1)]
list_coefficients2 = [random.randint(0, 100) for i in range(k2 + 1)]
file_write(file1_name, calculate_values(list_coefficients1))
file_write(file2_name, calculate_values(list_coefficients2))

list_from_file1 = file_read(file1_name)
list_from_file2 = file_read(file2_name)
print()
print(f"Первый многочлен {list_from_file1}")
print(f"Второй многочлен {list_from_file2}")
print()

list_coefficients_result = parse_polynomial()
file_write(file_result_name, calculate_values(list_coefficients_result))

list_from_file_result = file_read(file_result_name)
print(f"Сумма многочленов = {list_from_file_result}")
