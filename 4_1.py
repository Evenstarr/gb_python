# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

n = input("Введите целое положительное число: ")

'''
i = 0

maximum = int(n[0])
while i < len(n):
    if int(n[i]) > maximum:
        maximum = int(n[i])
    i += 1
'''
res = int(n)
tmp_max = 0
maximum = 0;

while res > 10:
    tmp_max = res % 10;
    if tmp_max > maximum:
        maximum = tmp_max;
    res = res // 10;

print(f"Самая большая цифра в числе - {maximum}")
