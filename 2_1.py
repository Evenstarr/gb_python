# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = [1, True, 'а', 1.15, None, 1+2j, ["a", "b"], ("1", 15), {'a', 'k', 'b', 'd', 'r'},
        {'key_1': 'val_1', 'key_2': 'val_2'}, b'bytes', bytearray(b'hello world!'), TypeError]

for el in list:
    print(type(el))
