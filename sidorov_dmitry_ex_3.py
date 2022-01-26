class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, line_len):
        result = ['*' * line_len] * (self.nums // line_len)
        if self.nums % line_len:
            result.append('*' * (self.nums % line_len))
        return '\n'.join(result)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        return f'{Cell(self.nums + other.nums)}'

    def __sub__(self, other):
        if self.nums < other.nums:
            raise ValueError('Вычитаение не возможно. Уменьшаемое меньше вычитаемого.')
        else:
            return f'{Cell(self.nums - other.nums)}'

    def __mul__(self, other):
        return f'{Cell(self.nums * other.nums)}'

    def __truediv__(self, other):
        if other.nums:
            return f'{(Cell(self.nums / other.nums))}'
        else:
            raise ZeroDivisionError('Операция невозможна. На ноль делить нельзя')

    def __floordiv__(self, other):
        if other.nums:
            return f'{(Cell(self.nums // other.nums))}'
        else:
            raise ZeroDivisionError('Операция невозможна. На ноль делить нельзя')

c1 = Cell(15)
c2 = Cell(2)
c3 = Cell(22)
c4 = Cell(0)
print(c1 + c2)
# print(c1 - c3)    # проверка вычитания из меньшего числа большего
print(c1 - c2)
print(c1 * c2)
# print(c1 // c4)  # проверка деления на 0
print(c2.make_order(8))
