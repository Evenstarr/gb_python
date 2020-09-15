# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(*args):
    try:
        numbers = [float(x) for x in list(args)]
        min_val = min(numbers)
        numbers.remove(min_val)
        return f'{sum(numbers):0.2f}'
    except (TypeError, ValueError):
        return "Не будем суммировать строки с числами. "


# раз речь о сумме, пусть будут числа
args_input = input("Введите 3 числа через пробел: ").split()

if len(args_input) == 3:
    print(my_func(*args_input))
else:
    print("Ввели не 3 аргумента")
