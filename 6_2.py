class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_full(self, mass=25, thickness=5):
        return f"{(self._length * self._width * mass * thickness) / 1000} t"


road = Road(20, 5000)
print(road.mass_full())
