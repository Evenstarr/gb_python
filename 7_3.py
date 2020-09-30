class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return self.cell - other.cell
        else:
            # Было в пояснениях в вебинаре
            return other.cell - self.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return self.cell // other.cell

    def make_order(self, rows):
        return ("*" * rows + "\n") * (self.cell // rows) + "*" * (self.cell % rows)


cell_1 = Cell(11)
cell_2 = Cell(5)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)

print(cell_1.make_order(4))
