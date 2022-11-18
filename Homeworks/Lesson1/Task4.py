"""

Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).

"""

correct_value = False
while not correct_value:
    try:
        quarter = int(input(f"Введите номер четверти: "))
        correct_value = True
    except ValueError:
        print("Ошибка: Введено не корректное значение")

if quarter == 1:
    print(f"x ∈ (0; +∞) y ∈ (0; +∞)")
elif quarter == 2:
    print(f"x ∈ (-∞; 0) y ∈ (0; +∞)")
elif quarter == 3:
    print(f"x ∈ (-∞; 0) y ∈ (-∞; 0)")
elif quarter == 4:
    print(f"x ∈ (0; +∞) y ∈ (-∞; 0)")
