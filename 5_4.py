# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# https://pypi.org/project/translate/


from translate import Translator


translator = Translator(from_lang="en", to_lang="ru")

lines = []

with open("text4_input.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        l_line = line.split()
        # баг переводчика
        if l_line[0] == "Four":
            l_line[0] = "Четыре"
        else:
            l_line[0] = translator.translate(l_line[0])
        lines.append(f"{' '.join(l_line)}\n")

with open("text4_output.txt", "w", encoding="utf-8") as f_obj:
    f_obj.writelines(lines)
