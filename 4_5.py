# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


from functools import reduce


def multiply_list(prev_el, el):
    return prev_el * el


initial_list = [x for x in range(100, 1001, 2)]

print(reduce(multiply_list, initial_list))
