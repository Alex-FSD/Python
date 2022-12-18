"""

3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа
элемента. Вносить его в список, только если введено число. Класс-исключение должен не
позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.

"""


class ValidValue:
    def __init__(self):
        self.valid_list = []

    def input_value(self):
        is_cycle = True
        while is_cycle:
            try:
                value = input("Введите число:")
                if value.lower() == "quit":
                    is_cycle = False
                else:
                    value = int(value)
                    self.valid_list.append(value)
            except ValueError:
                print(f"Недопустимое значение")
        return self.valid_list


print("Для выхода, введите 'quit'")
valid_value = ValidValue()
print(f"Список: {valid_value.input_value()}")
