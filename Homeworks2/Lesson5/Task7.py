"""

7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

"""

import json

profit = {}
profit_average = {}

lst = [
    "Фирма1 ООО 100000 50000",
    "Фирма2 ИП 10000 35000",
    "Фирма3 ЗАО 70000 10000",
    "Фирма4 ООО 37500 40000",
    "Фирма5 ИП 60000 22500",
]

with open("task7.txt", "w", encoding="utf-8") as my_f:
    for i in lst:
        my_f.write(i + "\n")

with open("task7.txt", "r", encoding="utf-8") as my_f:
    prf = 0
    prf_avg = 0
    i = 0
    for line in my_f:
        name, firm, revenue, losses = line.split()
        profit[name] = int(revenue) - int(losses)
        if profit.get(name) >= 0:
            prf = prf + profit.get(name)
            i += 1
    if i != 0:
        prf_avg = prf / i
        print(f"Средняя прибыль: {prf_avg:.2f}")
    else:
        print(f"Все работают в убыток")
    profit_average = {"средняя прибыль": round(prf_avg)}
    profit.update(profit_average)
    print(f"Прибыль каждой компании: {profit}")

with open("task7.json", "w", encoding="utf-8") as my_f:
    json.dump(profit, my_f, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': '))

    js_str = json.dumps(profit, ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': '))
    print(f"Создан файл с расширением json со следующим содержимым: \n "
          f" {js_str}")
