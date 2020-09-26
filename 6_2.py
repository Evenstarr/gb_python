class Road:
    asphalt_mass = 25
    road_depth = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self):
        mass = self._length * self._width * self.asphalt_mass * self.road_depth / 1000
        print(mass)


r = Road(20, 5000)
r.calculate_mass()
