# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

num_goods = int(input("Введите количество товаров: "))
list_goods = []
goods_data = ("название", "цена", "количество", "ед")

for i in range(1, num_goods + 1):
    goods_dict_data = {}
    for datum in goods_data:
        p = input(f"Ввведите {datum} для товара {i}: ")
        goods_dict_data[datum] = p
    list_goods.append((i, goods_dict_data))

print(list_goods)
print("Аналитика товаров: ")

analytics_data = {key: [] for key in goods_data}

for el in list_goods:
    for key, value in el[1].items():
        if value not in analytics_data[key]:
            analytics_data[key].append(value)

print(analytics_data)
