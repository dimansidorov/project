result = []     # создаем список
with open('nginx_logs.txt', 'r', encoding='utf-8') as file:    # открываем файл
    for row in file:
        line = row.split()     # сплитом разбиваем строку
        result.append((line[0], line[5][1:], line[6]))      # добавляем в список айпи, гет без передней кавычки и загрузку
print(result)