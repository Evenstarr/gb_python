# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = float(input("Введите выручку: "))
cost = float(input("Введите издержки: "))

is_profit = False

if income > cost:
    print("У вас прибыль")
    is_profit = True
else:
    print("У вас убыток")

if is_profit:
    print(f"Рентабельность - {(income - cost) / income}")
    employees_num = int(input("Введите численность сотрудников фирмы: "))
    print(f"Прибыль в расчете на одного сотрудника - {(income - cost) / employees_num}")
