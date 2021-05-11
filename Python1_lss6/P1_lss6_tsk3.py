
# 3. -------------------------------------

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.__income = dict(wage=wage, bonus=bonus)
        self.name = name
        self.surname = surname
        self.position = position

class Position(Worker):

    def get_full_name(self):
        print(self.name, ' ', self.surname)

    def get_total_income(self):
        # super().__init__(_Worker__income)
        print(self._Worker__income['wage'] + self._Worker__income['bonus'])

p = Position('John', 'Petrov', 'manager', 70000, 10000)

print(p._Worker__income)
p.get_full_name()
p.get_total_income()
