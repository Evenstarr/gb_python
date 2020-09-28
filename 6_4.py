class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} {self.color} - Go")

    def stop(self):
        print(f"{self.name} {self.color} - Stop")

    def turn(self, direction):
        if direction in ('right', 'left', 'back'):
            print(f"{self.name} {self.color} turned {direction}")
        else:
            print("Wrong direction")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости! ')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости! ')
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


policeCar = PoliceCar(100, "blue", "Mazda")
print(policeCar.is_police)
print(policeCar.name)
print(policeCar.color)
print(policeCar.speed)
policeCar.go()
policeCar.stop()
policeCar.turn("right")
policeCar.show_speed()


workCar = WorkCar(100, "yellow", "Kia")
workCar.go()
workCar.stop()
workCar.turn("opposite")
workCar.show_speed()
print(workCar.is_police)
print(workCar.name)
print(workCar.color)
print(workCar.speed)
