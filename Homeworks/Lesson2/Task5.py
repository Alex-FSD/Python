"""

Реализуйте алгоритм перемешивания списка.

"""

import random

list_simple = [random.randint(0, 10) for i in range(random.randint(5, 10))]
print(f"Исходный список: {list_simple}")
random.shuffle(list_simple)
print(f"Результат: {list_simple}")
