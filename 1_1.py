string_var = "string"
print(f"{string_var} - первая переменная - строка")

num_var = 1
print(f"Вторая переменная {num_var}, а еще вот так умеет - {num_var + 1}")

input_string = input("Введите что-то: ")
print(f"Вы ввели {input_string}")

input_int = int(input("А здесь введите цифру: "))

# А если здесь ввести не цифру, будет ошибка. Но Вы сказали, что то, что не проходили, не писать)
print(f"Вы ввели {input_int}")