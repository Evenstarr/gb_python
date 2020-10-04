class OfficeEquipment:
    def __init__(self, size, price, name):
        self.size = size
        self.price = price
        self.name = name


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        try:
            quantity = int(quantity)
            for _ in range(quantity):
                self.products.append(product)
        except (TypeError, ValueError):
            print("ERROR - Cant add - quantity not integer")

    def remove_product(self, product, quantity):
        cnt = 0

        try:
            quantity = int(quantity)

            for n in range(quantity):
                for ix, item in enumerate(self.products):
                    # Я знаю, что это плохо) И что у нас могут быть модели, имеющие те же самые параметры,
                    # отличающиеся аргументами классов. Тут надо думать.
                    if item.name == product.name and item.type == product.type and item.price == product.price \
                            and item.size == product.size:
                        del self.products[ix]
                        cnt += 1
                        break

            if cnt < quantity:
                print(f"На складе нет {quantity} '{product.type} {product.name}', отдали последнее - только {cnt}")
            else:
                print(f"Отдали в другие подразделения {quantity} '{product.type} {product.name}'")
        except (TypeError, ValueError):
            print("ERROR - Cant remove - quantity non integer")

    def __str__(self):
        s = ''
        for pr in self.products:
            s += "{}\n".format(pr)
            print("{}\n".format(pr))
        return s


class Printer(OfficeEquipment):
    def __init__(self, size, price, name, coloured=False, laser=True):
        super().__init__(size, price, name)
        self.coloured = coloured
        self.laser = laser
        self.type = "Принтер"

    def __str__(self):
        return f"Что это - {self.type}, название - {self.name}, цена - {self.price}, размер - {self.size}, цветной - {self.coloured}, " \
               f"лазерный - {self.laser}"


class Scanner(OfficeEquipment):
    def __init__(self, size, price, name, is_photo=False):
        super().__init__(size, price, name)
        self.is_photo = is_photo
        self.type = "Сканер"

    def __str__(self):
        return f"Что это - {self.type}, название - {self.name}, цена - {self.price}, размер - {self.size}, фото - {self.is_photo}"


class Monitor(OfficeEquipment):
    def __init__(self, kind, size, price, name, is_square=False):
        super().__init__(size, price, name)
        self.kind = kind
        self.is_square = is_square
        self.type = "Монитор"

    def __str__(self):
        return f"Что это - {self.type}, название - {self.name}, цена - {self.price}, " \
               f"размер - {self.size}, тип - {self.kind}, квадратный - {self.is_square}"


wh = Warehouse()

data_printer = input("Введите информацию о принтере через пробел - размер, цена, название, цветной, лазерный"
                     "(2 последних булевы): ").split()

printer = Printer(*data_printer)
printer_quantity = input("Количество таких принтеров: ")
wh.add_product(printer, printer_quantity)

data_scanner = input("Введите информацию о сканере через пробел - размер, цена, название, фотопринтер(булево): ").split()
scanner_quantity = input("Количество таких сканеров: ")

scanner = Scanner(*data_scanner)

wh.add_product(scanner, scanner_quantity)


data_monitor = input("Введите информацию о мониторе через пробел - тип, размер, цена, название: ").split()
monitor_quantity = input("Количество таких мониторов: ")
monitor = Monitor(*data_monitor)
wh.add_product(monitor, monitor_quantity)

print(wh)

remove_monitor = input("Сколько мониторов удалить? ")
wh.remove_product(monitor, remove_monitor)

print(wh)
