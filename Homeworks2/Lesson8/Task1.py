"""

1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.

"""


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    @classmethod
    def extract(cls, day_month_year):
        valid_date = []
        for i in day_month_year.split():
            if i != "-":
                valid_date.append(i)
        return Date.valid(int(valid_date[0]), int(valid_date[1]), int(valid_date[2]))

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2000 <= year <= 2022:
                    return f"Дата: {str(day).rjust(2, '0')}.{str(month).rjust(2, '0')}.{year}"
                else:
                    return f"Не допустимое значение: год"
            else:
                return f"Не допустимое значение: месяц"
        else:
            return f"Не допустимое значение: день"

    def __str__(self):
        return f"{Date.extract(self.day_month_year)}"


simple_date = Date("1 - 1 - 2001")
print(simple_date)

print(Date.extract("31 - 1 - 2021"))

print(Date.valid(1, 12, 2012))

simple_date = Date("32 - 1 - 2001")
print(simple_date)
simple_date = Date("1 - 13 - 2001")
print(simple_date)
simple_date = Date("1 - 1 - 1999")
print(simple_date)
