# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


if len(argv) < 4:
    print("Недостаточное количество параметров")
else:
    try:
        print(f'{float(argv[1]) * float(argv[2]) + float(argv[3]):0.2f}')
    except TypeError:
        print('Неверные значения параметров')
