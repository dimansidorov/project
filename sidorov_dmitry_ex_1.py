from time import sleep as sl


class TrafficLight:

    def running(self):
        while True:
            self.__color = 'Красный'
            print(self.__color)
            sl(7)
            self.__color = 'Желтый'
            print(self.__color)
            sl(2)
            self.__color = 'Зеленый'
            print(self.__color)
            sl(7)


t = TrafficLight()
t.running()
