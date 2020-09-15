# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def pack_user_data(**kwargs):
    return ", ".join(list(kwargs.values()))


user_data = {
    "name": "Вася",
    "surname": "Пупкин",
    "birth_year": "1990",
    "city": "Урюпинск",
    "email": "vasya1990@mail.ru",
    "phone": "125030"
}

# В условии не требуется ввод данных от пользователя. Он был бы таким же, как в 6 задаче урока 2
print(pack_user_data(**user_data))
