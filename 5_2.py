# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open('text2.txt', encoding="utf-8") as f_obj:
    lines = f_obj.readlines()

print(f'Количество строк - {len(lines)}')

for i in range(len(lines)):
    print(f'В строке {i + 1} {len(lines[i].split())} слов')
