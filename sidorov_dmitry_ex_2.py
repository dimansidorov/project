from abc import ABC, abstractmethod


class Clothes(ABC):
    expence_summary = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.expence_summary += self.expence


    def __str__(self):
        return f'На пальто размера {self.size} уйдет {round(self.expence, 1)} погонных метров ткани\n' \
               f'Общий расход ткани: {round(Coat.expence_summary, 1)} погонных метров.'


    @property
    def expence(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.expence_summary += self.expence


    def __str__(self):
        return f'На костюм рост {self.height} уйдет {round(self.expence, 1)} погонных метров ткани\n' \
               f'Общий расход ткани: {round(Suit.expence_summary, 1)} погонных метров.'

    @property
    def expence(self):
        return (2 * self.height + 0.3) / 100


clothes_one = Coat(48)
print(clothes_one)
clothes_two = Suit(176)
print(clothes_two)
clothes_three = Suit(190)
print(clothes_three)
clothes_four = Coat(58)
print(clothes_four)