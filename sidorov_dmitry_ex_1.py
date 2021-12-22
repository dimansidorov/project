def odd_to(number):     # создаем функцию
    for num in range(1, number + 1, 2):
        yield num

n = odd_to(10)
print(type(n))  # проверяем тип
print(*n)   # распаковываем
