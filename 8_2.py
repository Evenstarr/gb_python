class OwnZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


input_str = input("Введите 2 числа через пробел: ")

try:
    numbers = list(map(float, input_str.split()))
    if len(numbers) > 2:
        raise ValueError
    else:
        if numbers[1] == 0:
            raise OwnZeroDivisionError("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода")
except OwnZeroDivisionError as err:
    print(err)
else:
    print(input_str)
