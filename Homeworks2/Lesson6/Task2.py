"""

2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500т.

"""


class Road:
    _width = None
    _length = None
    mass = None
    thickness = None

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def consumption(self):
        self.mass = 25
        self.thickness = 5
        consumption = self.width * self.length * self.mass * self.thickness / 1000
        print(f"{self.width}м * {self.length}м * {self.mass}кг * {self.thickness}см = {consumption:.0f}т")


road_under_construction = Road(20, 5000)
road_under_construction.consumption()
