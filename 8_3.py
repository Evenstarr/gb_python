class NotNumBerException(Exception):
    def __init__(self, txt):
        self.txt = txt


num_list = []

while True:
    num = input("Введите что-то или stop: ").strip()  # Было бы нехорошо, если б не пропускало число + пробел

    if num == "stop":
        break
    try:
        if num.isdigit():
            num_list.append(num)
        else:
            raise NotNumBerException("Ввели не число")
    except NotNumBerException as err:
        print(err)

print(num_list)
