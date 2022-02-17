class Worker:

    def __init__(self, surname, name, position, profit, bonus):
        self.surname = surname
        self.name = name
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, surname, name, position, profit, bonus):
        super().__init__(surname, name, position, profit, bonus)
    def get_full_name(self):
        return self.surname + self.name
    def get_full_profit(self):
        self.__income = {'profit': self.profit, 'bonus': self.bonus}
        return self.__income

manager = Position('Ivanov', 'Ivan', 'manager',50000 , 100000)
print(manager.get_full_name(), manager.get_full_profit())