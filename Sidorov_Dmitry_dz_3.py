percent_list = []  # создаем пустой список

for percent in range(1, 101):
    percent_list.append(int(percent))  # добавляем в него целые числа (int) от 1 до 100

for percent in percent_list:
    if percent % 10 == 1 and percent != 11:  # числа, которые кончаются на 1, кроме 11
        print(percent, 'процент')
    elif 2 <= percent % 10 <= 4 and percent != 12 and percent != 13 and percent != 14:
        # числа, которые заканчиваются на 3, 4, 5, кроме 12, 13, 14
        print(percent, 'процента')
    else:   # все остальные числа
        print(percent, 'процентов')
