# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

input_str = []

x = input("Введите строку. Для окончания нажмите enter: ")
while x:
    input_str.append(f'{x}\n')
    x = input("Введите строку. Для окончания нажмите enter: ")


with open("text1.txt", "w", encoding="utf-8") as f_obj:
    f_obj.writelines(input_str)
