"""

4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.

"""


class Car:
    # attributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn_right(self):
        return f"{self.name} повернула направо"

    def turn_left(self):
        return f"{self.name} повернула налево"

    def show_speed(self):
        return f"Текущая скорость {self.name} = {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость городского автомобиля {self.name} = {self.speed}")

        if self.speed > 40:
            return f"Скорость {self.name} выше, чем допустимо для городского автомобиля"
        else:
            return f"Скорость {self.name} нормальная для городского автомобиля"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость рабочего автомобиля {self.name} = {self.speed}")

        if self.speed > 60:
            return f"Скорость {self.name} выше, чем допустимо для рабочих машины"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} это полицейский автомобиль"
        else:
            return f"{self.name} это не полицейский автомобиль"


audi = SportCar(100, "Красная", "Audi", False)
toyota = TownCar(30, "Белая", "Toyota", False)
lada = WorkCar(70, "Черная", "Lada", True)
ford = PoliceCar(110, "Синий", "Ford", True)

print(lada.turn_left())
print(f"Когда {toyota.turn_right()}, то {audi.stop()}")
print(f"{lada.go()}. {lada.show_speed()}")
print(f"{lada.name} {lada.color}")
print(f"{audi.name} полицейская? {audi.is_police}")
print(f"{lada.name} полицейская? {lada.is_police}")

print(audi.show_speed())
print(toyota.show_speed())
print(ford.police())
print(ford.show_speed())
