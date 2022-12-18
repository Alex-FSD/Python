"""

2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.

"""


class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    catalog_coat = []

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size
        self.consumption_coat = round(size / 6.5 + 0.5, 2)
        self.catalog_coat.append([name, size, self.consumption_coat])

    def __str__(self):
        return f"{self.name}, размер = {self.size}"

    @property
    def get_consumption_coat(self):
        return f"Расход ткани на {self.name} = {round(self.size / 6.5 + 0.5, 2)}"

    @property
    def get_consumption_full(self):
        total_consumption = 0.0
        for i in self.catalog_coat:
            total_consumption += i[2]
        return str(f"Общий расход ткани на пальто: {total_consumption:.2f}")


class Jacket(Clothes):
    catalog_jacket = []

    def __init__(self, name, height):
        super().__init__(name)
        self.height = height
        self.consumption_jacket = round(height * 2 + 0.3, 2)
        self.catalog_jacket.append([name, height, self.consumption_jacket])

    def __str__(self):
        return f"{self.name}, рост = {self.height}"

    @property
    def get_consumption_jacket(self):
        return f"Расход ткани на {self.name} = {round(self.height * 2 + 0.3, 2)}"

    @property
    def get_consumption_full(self):
        total_consumption = 0.0
        for i in self.catalog_jacket:
            total_consumption += i[2]
        return str(f"Общий расход ткани на костюмы: {total_consumption:.2f}")


coat1 = Coat("Пальто 1", 32)
coat2 = Coat("Пальто 2", 34)
coat3 = Coat("Пальто 3", 30)
coat4 = Coat("Пальто 4", 36)
coat5 = Coat("Пальто 5", 32)
jacket1 = Jacket("Костюм 1", 1.82)
jacket2 = Jacket("Костюм 2", 1.76)
jacket3 = Jacket("Костюм 3", 1.62)
jacket4 = Jacket("Костюм 4", 1.72)
jacket5 = Jacket("Костюм 5", 1.80)
catalog_full = [coat1, coat2, coat3, coat4, coat5,
                jacket1, jacket2, jacket3, jacket4, jacket5]
for i in catalog_full:
    print(i)
print()
for i in catalog_full:
    if i.__class__ == Coat:
        print(i.get_consumption_coat)
    if i.__class__ == Jacket:
        print(i.get_consumption_jacket)
print()
print(coat1.get_consumption_full)
print(jacket1.get_consumption_full)
