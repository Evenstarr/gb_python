# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

salary = 0
count_lines = 0
with open("text3.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        splitting = line.split()
        try:
            if float(splitting[1]) < 20000:
                print(f"У сотрудника {splitting[0]} оклад меньше 20К")
            salary += float(splitting[1])
        except (TypeError, ValueError):
            print(f"Невозможно определить зарплату сотрудника {splitting[0]}")
        count_lines += 1


print(f"Средняя величина дохода сотрудников - {(salary/count_lines):0.2f}")
