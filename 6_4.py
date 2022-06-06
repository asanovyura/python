class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} is started"

    def stop(self):
        return f"{self.name} is stop"

    def turn_left(self):
        return f"{self.name} is turn left"

    def turn_right(self):
        return f"{self.name} is turn right"

    def show_speed(self):
        return f"Speed {self.name} is {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Speed of town car {self.name} is {self.speed}")

        if self.speed > 60:
            return f"Speed of {self.name} is higher than allow for town car"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Speed of work car {self.name} is {self.speed}")

        if self.speed > 40:
            return f"Speed of {self.name} is higher than allow for work car"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} is from police department"


Lamborghini = SportCar(250, "Red", "Lamborghini", False)
mercedes = TownCar(50, 'White', 'Mercedes', False)
wolksvagen = WorkCar(60, "navy blue", "Wolksvagen", True)
ford = PoliceCar(100, "yellow", "Ford", True)
print(wolksvagen.turn_left())
print(f"When {mercedes.turn_right()}, then {Lamborghini.stop()}")
print(f"{wolksvagen.go()} with speed exactly {wolksvagen.show_speed()}")
print(f"{wolksvagen.name} is {wolksvagen.color}")
print(f"Is {Lamborghini.name} a police car? {Lamborghini.is_police}")
print(f'Is {wolksvagen.name}  a police car? {wolksvagen.is_police}')
print(Lamborghini.show_speed())
print(mercedes.show_speed())
print(ford.police())
print(ford.show_speed())
