class Car:
    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police
        print(f'Автомобиль: \nМодель - {self.name};\n'
              f'Цвет - {self.color};\n'
              f'{"Полицеский" if is_police else "Граждаский"} автомобиль.')

    def go(self, speed):
        self.speed = speed
        print(f'Автомобиль {self.name} тронулся с места. Скорость - {self.speed} км/ч .')

    def stop(self, speed=0):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился.')

    def turn(self, direction):
        self.direction = direction
        print(f'Автомобиль {self.name} повернул {self.direction}')


class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        print(
            f'Внимание! Превышение скорости! Ваша скорость {self.speed} км/ч. Разрешенная скорость 60 км/ч.' if self.speed > 60 else
            f'Ваша скорость {self.speed} км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        print(
            f'Внимание! Превышение скорости! Ваша скорость {self.speed} км/ч. Разрешенная скорость 40 км/ч.' if self.speed > 40 else
            f'Ваша скорость {self.speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, name, color, is_police=True):
        super(PoliceCar, self).__init__(name, color, is_police)


car_1 = SportCar('Lamborghini', 'White')
car_1.go(120)
car_1.turn('налево')
car_1.stop()
print('*' * 20)
car_2 = PoliceCar('Mercedes', 'White')
car_2.go(80)
print('*' * 20)
car_3 = WorkCar('Gaz', 'White')
car_3.show_speed(60)
print('*' * 20)
car_4 = TownCar('KIA', 'Green')
car_4.show_speed(59)
