class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки. - Stationary")


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Draw with a pen")


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Draw with a pencil")


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print("Draw with a handle")


base = Stationary("Common")
base.draw()

pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандашик")
pencil.draw()

handle = Handle("Маркер?")
handle.draw()

