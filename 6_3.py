class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def full_name(self):
        return f"Full name {self.name} {self.surname}"
    def full_profit(self):
        return sum(self._income.values())


best_worker = Position("Chuck", "Norris", "head of security position", 9999999, 111111111)
print(best_worker.full_name())
print(best_worker.position)
print(best_worker.full_profit())