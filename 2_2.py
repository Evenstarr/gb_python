# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_to_change = input("Введите список через пробел: ").split()
print(list_to_change)

index_to_change = 0

for n in range(0, len(list_to_change)):
    if index_to_change < len(list_to_change) - 1:
        list_to_change[index_to_change], list_to_change[index_to_change + 1] = list_to_change[index_to_change + 1], list_to_change[index_to_change]
        index_to_change += 2

print(list_to_change)