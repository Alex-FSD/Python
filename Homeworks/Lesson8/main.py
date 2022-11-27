"""

Доделать решение задачи: Задача:
Создать информационную систему, позволяющую работать с сотрудниками некой компании
\ студентами вуза \ учениками школы

"""

import data_handling as dh


def input_action():
    prog_exec = True
    print("\nМеню:\n\
    1 - Показать справочник\n\
    2 - Добавить контакт\n\
    3 - Редактировать контакт\n\
    4 - Удалить контакт\n\
    5 - Поиск контакта\n\
    6 - Экспорт данных\n\
    exit - Выход\n")
    choose = input("Выберите действие: ")
    if choose == "1":
        dh.print_data()
    elif choose == "2":
        dh.import_record(dh.input_data())
    elif choose == "3":
        dh.edit_data()
    elif choose == "4":
        dh.remove_data()
    elif choose == "5":
        dh.print_record()
    elif choose == "6":
        dh.export_data()
    elif choose == "exit":
        prog_exec = False
    return prog_exec


program_execution = True
while program_execution:
    program_execution = input_action()
