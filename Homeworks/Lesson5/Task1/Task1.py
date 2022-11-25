"""

Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

Входные и выходные данные хранятся в отдельных текстовых файлах.

"""


def file_write(name, s):
    with open(name, "w") as data:
        data.write(s)


def file_read(name):
    with open(name, "r") as data:
        return data.read()


file1_name: str = "file1.txt"
file2_name: str = "file2.txt"

text = "Мама мыло абвраму, а папа мыл абвдверь"
file_write(file1_name, text)

text = file_read(file1_name)
print(f'Входные данные: {text}')
text_find = "абв"

text = text.split()
for i in range(len(text)):
    if text_find in text[i]:
        if not text[i].isidentifier():
            text[i] = text[i][-1]
        else:
            text[i] = ""
text.remove("")
text = " ".join(text)
file_write(file2_name, text)

print(f'Результат: {text}')
