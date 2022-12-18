"""

7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.

"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a) - (self.b * other.b), self.b * other.a)

    def __str__(self):
        return f"({self.a} + {self.b}j)"


z_1 = ComplexNumber(2, 3)
z_2 = ComplexNumber(4, 5)
print(z_1)
print(z_2)
print()
print("Сложение:")
print(z_1 + z_2)
print("Умножение:")
print(z_1 * z_2)
print()
print("Проверка:")
print(complex(2, 3) + complex(4, 5))
print(complex(2, 3) * complex(4, 5))
