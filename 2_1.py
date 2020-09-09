# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

sec = int(input("Введите время в секундах: "))

hours = sec // 3600
minutes = (sec - hours * 3600) // 60
seconds = sec - hours * 3600 - minutes * 60

if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)

print(f'Введенное время - {hours}:{minutes}:{seconds}')
