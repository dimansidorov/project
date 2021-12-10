prices = [167.84, 56.17, 98.8, 25.1, 196, 299.99, 55.25, 85, 54.90, 96, 156.99, 360.87, 99.9, 1299]
print(f'ID списка: {id(prices)}')
prices.sort()   # используем метод sort
# print(prices) # смотрим изменился ли список
print(f'ID отсортированного списка: {id(prices)}')
for price in prices:
    rr = int(price)
    kk = (price - rr) * 100
    print(f'{rr} рублей {kk:02.0f} копеек')


prices = [167.84, 56.17, 98.8, 25.1, 196, 299.99, 55.25, 85, 54.90, 96, 156.99, 360.87, 99.9, 1299]
prices_reverse = sorted(prices, reverse=True)[:5]   # используем метод sorted
for price in prices_reverse:
    rr = int(price)
    kk = (price - rr) * 100
    print(f'{rr} рублей {kk:02.0f} копеек', end='; ')  # в одну линию
    # сделал точку с запятой, т.к. очень коряво смотрится конец черз запятую
