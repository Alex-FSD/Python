"""

4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.


5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).


6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

"""


class StoreOfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store = []
        self.my_unit = {"Модель устройства": self.name, "Цена за ед": self.price, "Количество": self.quantity}

    def __str__(self):
        return f"{self.name} цена {self.price} количество {self.quantity}"

    def reception(self):
        is_valid = True
        while is_valid:
            try:
                unit = input(f"Введите наименование: ")
                unit_p = int(input(f"Введите цену за ед: "))
                unit_q = int(input(f"Введите количество: "))
                unique = {"Модель устройства": unit, "Цена за ед": unit_p, "Количество": unit_q}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                is_valid = False
            except ValueError:
                print("Ошибка: Некорректное значение")

        is_quit = input("Для выхода, введите 'quit'\n"
                        "Для продолжения,нажмите Enter\n"
                        "---> ")
        if is_quit.lower() == "quit":
            return f"Весь склад: \n {self.my_store}"
        else:
            return StoreOfficeEquipment.reception(self)


class Printer(StoreOfficeEquipment):
    def to_print(self):
        return f"Ресурс принтера: {self.numb} страниц"


class Scanner(StoreOfficeEquipment):
    def to_scan(self):
        return f"Ресурс сканера: {self.numb} использований"


class Copier(StoreOfficeEquipment):
    def to_copier(self):
        return f"Ресурс ксерокса: {self.numb} использований"


unit_1 = Printer("hp", 2000, 5, 1600)
unit_2 = Scanner("Canon", 1200, 5, 100000)
unit_3 = Copier("Xerox", 1500, 1, 150000)
print(StoreOfficeEquipment.reception(unit_1))
print()
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())
