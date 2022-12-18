"""

4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.

"""

lst = [
    "One — 1",
    "Two — 2",
    "Three — 3",
    "Four — 4"
]

with open("task4.txt", "w", encoding="utf-8") as my_f:
    for i in lst:
        my_f.write(i + "\n")

rus = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

lst = []
with open("task4.txt", "r", encoding="utf-8") as my_f:
    for i in my_f:
        i = i.split(" ", 1)
        lst.append(rus[i[0]] + " " + i[1])

with open("task4_1.txt", "w", encoding="utf-8") as my_f:
    my_f.writelines(lst)
