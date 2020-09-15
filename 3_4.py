# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(x, y):
    errors = []
    try:
        x = float(x)
    except ValueError:
        errors.append("Первое число не действительное")
    else:
        if x <= 0:
            errors.append("Первое число не положительное")
    try:
        y = int(y)
    except ValueError:
        errors.append("Второе число не целое")
    else:
        if y >= 0:
            errors.append("Второе число не отрицательное")
    if len(errors) > 0:
        return ", ".join(errors)
    else:
        new_pow = 1
        for i in range(abs(y)):
            new_pow *= x
        return f"1 способ - {x**y:0.5f}, 2 способ - {1 / new_pow:0.5f}"


num1 = input("Введите действительное положительное число: ")
num2 = input("Введите целое отрицательное число: ")

print(my_func(num1, num2))
