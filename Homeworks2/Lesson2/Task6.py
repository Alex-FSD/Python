"""

6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя.

Пример готовой структуры:
[
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например, название. Тогда значение — список
значений-характеристик, например, список названий товаров.

Пример:
{
"название": ["компьютер", "принтер", "сканер"],
"цена": [20000, 6000, 2000],
"количество": [5, 2, 7],
"ед": ["шт."]
}

"""

s1 = "Наименование"
s2 = "Цена"
s3 = "Количество"
s4 = "Единица"

lst = [
    (1, {s1: "Компьютер", s2: 20000, s3: 5, s4: "шт."}),
    (2, {s1: "Принтер", s2: 6000, s3: 2, s4: "шт."}),
    (3, {s1: "Сканер", s2: 2000, s3: 7, s4: "шт."})
]

dct = {
    s1: [],
    s2: [],
    s3: [],
    s4: []
}
for i in lst:
    dct[s1].append(i[1][s1])
    dct[s2].append(i[1][s2])
    dct[s3].append(i[1][s3])
    dct[s4].append(i[1][s4])

print(dct)