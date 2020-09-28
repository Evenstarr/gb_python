class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки. - Stationary {self.title}")


class Pen(Stationary):
    def draw(self):
        print(f"Draw with a pen {self.title}")


class Pencil(Stationary):
    def draw(self):
        print(f"Draw with a pencil {self.title}")


class Handle(Stationary):
    def draw(self):
        print(f"Draw with a handle {self.title}")


base = Stationary("Common")
base.draw()

pen = Pen("Ручка")
pen.draw()

pencil = Pencil("Карандашик")
pencil.draw()

handle = Handle("Маркер?")
handle.draw()

