ip_dict = {}    # создаем словарь
with open('nginx_logs.txt', 'r', encoding= 'utf-8') as file:    # открываем файл
    for row in file:
        line = row.split()      # сплитом разбиваем строку
        ip_ad = line[0]     # получаем id-адрес
        if ip_ad in ip_dict:    # словарь, в котором ключи - адреса, а значения - счетчики запросов с этих адресов
            ip_dict[ip_ad] += 1
        else:
            ip_dict[ip_ad] = 1
max_requests = max(ip_dict.values())    # находим максимальное колличество запросов
for key, val in ip_dict.items():
    if val == max_requests:
        print(f'IP-адрес спамера: {key} ; \nКолличество запросов: {val}.')