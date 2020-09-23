# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


with open("text5.txt", "w") as f_obj:
    initial_list = [str(randint(1, 30)) for x in range(0, 20)]
    f_obj.writelines(" ".join(initial_list))

print(initial_list)

with open("text5.txt") as f_read_obj:
    for line in f_read_obj:
        try:
            # В условии одна строка)
            n_list = map(int, line.split())
            print(sum(n_list))
        except (TypeError, ValueError):
            print("Введено непонятно что")
