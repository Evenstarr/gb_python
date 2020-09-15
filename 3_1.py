# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(a, b):
    try:
        return f'{(float(a) / float(b)):0.2f}'
    except ZeroDivisionError:
        return "На ноль делить плохо!"
    except ValueError:
        return "Ввели не числа, их тоже не делим"


try:
    args = input("Введите 2 числа через пробел: ").split()
    print(f"Результат деления введенных чисел - {division(*args)}")
except (ValueError, TypeError):
    print("Ввели что-то не то. Нужно 2 числа через пробел")
