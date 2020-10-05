class OfficeEquipment:
    def __init__(self, barcode, size, price, name):
        self.size = size
        self.price = price
        self.name = name
        self.barcode = barcode


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        try:
            quantity = int(quantity)
            self.products.append([product, quantity])
        except (TypeError, ValueError):
            print("ERROR - Cant add - quantity not integer")

    def remove_product(self, product, quantity):
        try:
            quantity = int(quantity)

            for idx, item in enumerate(self.products):
                if item[0].barcode == product.barcode:
                    if quantity >= item[1]:
                        print(f"отдали последние - {item[1]} '{product.type} {product.name}'")
                        # раз не осталось таких - убираем
                        del self.products[idx]
                    else:
                        print(f"Отдали в другие подразделения {quantity} '{product.type} {product.name}'")
                        self.products[idx] = [item[0], item[1] - quantity]
        except (TypeError, ValueError):
            print("ERROR - Cant remove - quantity non integer")

    def __str__(self):
        s = ''
        for pr in self.products:
            s += "{} ({})\n".format(pr[0], pr[1])
        return s


class Printer(OfficeEquipment):
    def __init__(self, barcode, size, price, name, coloured=False, laser=True):
        super().__init__(barcode, size, price, name)
        self.coloured = coloured
        self.laser = laser
        self.type = "Принтер"

    def __str__(self):
        return f"Что это - {self.type}, штрихкод - {self.barcode}, название - {self.name}, цена - {self.price}, размер - {self.size}, цветной - {self.coloured}, " \
               f"лазерный - {self.laser}"


class Scanner(OfficeEquipment):
    def __init__(self, barcode, size, price, name, is_photo=False):
        super().__init__(barcode, size, price, name)
        self.is_photo = is_photo
        self.type = "Сканер"

    def __str__(self):
        return f"Что это - {self.type}, штрихкод - {self.barcode}, название - {self.name}, цена - {self.price}, " \
               f"размер - {self.size}, фото - {self.is_photo}"


class Monitor(OfficeEquipment):
    def __init__(self, barcode, kind, size, price, name, is_square=False):
        super().__init__(barcode, size, price, name)
        self.kind = kind
        self.is_square = is_square
        self.type = "Монитор"

    def __str__(self):
        return f"Что это - {self.type}, штрихкод - {self.barcode}, название - {self.name}, цена - {self.price}, " \
               f"размер - {self.size}, тип - {self.kind}, квадратный - {self.is_square}"


wh = Warehouse()

data_printer = input("Введите информацию о принтере через пробел - штрихкод, размер, цена, название, цветной, лазерный"
                     "(2 последних булевы): ").split()

printer = Printer(*data_printer)
printer_quantity = input("Количество таких принтеров: ")
# printer = Printer(123, 50, 50, 'Canon', True, True)
# printer_quantity = 5
wh.add_product(printer, printer_quantity)
#
data_scanner = input("Введите информацию о сканере через пробел - штрихкод, "
                     "размер, цена, название, фотопринтер(булево): ").split()
scanner_quantity = input("Количество таких сканеров: ")

scanner = Scanner(*data_scanner)

# scanner = Scanner(456, 100, 100, 'Nikon', True)
# scanner_quantity = 2
wh.add_product(scanner, scanner_quantity)
#
#
data_monitor = input("Введите информацию о мониторе через пробел - штрихкод, тип, размер, цена, название: ").split()
monitor_quantity = input("Количество таких мониторов: ")
monitor = Monitor(*data_monitor)

# monitor = Monitor(789, 'LCD', 20, 200, 'Samsung', False)
# monitor_quantity = 3
wh.add_product(monitor, monitor_quantity)

print(wh)

remove_monitor = input("Сколько мониторов удалить? ")
wh.remove_product(monitor, remove_monitor)

print(wh)
