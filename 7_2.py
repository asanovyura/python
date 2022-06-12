from abc import ABC, abstractmethod


class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def conseption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.conseption + other.conseption
        return Costume(0)

    def __str__(self):
        res = Clothes.result
        Clothes.result = 0
        return f"{res}"


class Coat(Clothes):
    @property
    def conseption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def conseption(self):
        return round(2 * self.param) + 0.3


coat = Coat(12)
costume = Costume(22)
print(coat + costume)
