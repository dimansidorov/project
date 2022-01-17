class Stationery:
    def __init__(self, title="Фиргуры"):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} маркером')

picture_1 = Pencil('треугольника')
picture_1.draw()
picture_2 = Pen('треугольника')
picture_2.draw()
picture_3 = Handle('треугольника')
picture_3.draw()