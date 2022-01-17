class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Фамилия: {self.surname} \nИмя: {self.name}'

    def get_total_income(self):
        return f"Общий доход: {self._income['wage'] + self._income['bonus']} рублей"

backend_developer = Position('Дмитрий', 'Сидоров', 'Backend-разработчик', 90000, 35000)
print(backend_developer.get_full_name())
print(backend_developer.get_total_income())

