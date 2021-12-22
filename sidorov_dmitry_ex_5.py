src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()  # множество уникальных
non_unique = set()  # множество повторов
for i in src:   # циклом проходим по списку и разделяем его элементы по множестам
    if i in non_unique or i in unique:
        unique.discard(i)
        non_unique.add(i)
    else:
        unique.add(i)
result = sorted((el for el in unique), key=src.index)   # сортируем по ключу индекса списка
print(result)