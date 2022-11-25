"""

Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

Входные и выходные данные хранятся в отдельных текстовых файлах.

"""


def file_write(name, s):
    with open(name, "w") as data:
        data.write(s)


def file_read(name):
    with open(name, "r") as data:
        return data.read()


def coding(txt):
    result = ''
    prev_char = ''
    count = 1
    for char in txt:
        if char != prev_char:
            if prev_char:
                result += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return result


def decoding(txt):
    count = ''
    result = ''
    for char in txt:
        if char.isdigit():
            count += char
        else:
            result += char * int(count)
            count = ''
    return result


file1_name: str = "file1.txt"
file2_name: str = "file2.txt"

text = "aaabbbbbcddddddeeffff"
print(f'Входные данные: {text}')
print()

file_write(file1_name, coding(text))
text = file_read(file1_name)
print(f"Текст после сжатия данных: {text}")

file_write(file2_name, decoding(text))
text = file_read(file2_name)
print(f"Текст после восстановления данных: {text}")
