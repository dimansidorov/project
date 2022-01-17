class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass(self):
        return f'{self._lenght} м * {self._width} м * 25 кг * 5 см = {int(self._lenght * self._width * 25 * 5 / 1000)} т'

r_1 = Road(5000, 20)
print(r_1.mass())