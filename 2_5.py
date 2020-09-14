 #5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 # У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
 # то новый элемент с тем же значением должен разместиться после них.

rating = [7, 5, 3, 3, 2]
print(rating)

next_el = None

while True:
    next_el = input("Введите новый элемент рейтинга. Если надоело, напишите Quit: ")

    if next_el == "Quit":
        break

    next_el = int(next_el)
    if next_el in rating:
        pos = len(rating) - list(reversed(rating)).index(next_el) - 1
        rating.insert(pos + 1, next_el)
    else:
        for el in rating:
            if next_el > el:
                rating.insert(rating.index(el), next_el)
                break
        if next_el not in rating:
            rating.append(next_el)

    print(rating)
