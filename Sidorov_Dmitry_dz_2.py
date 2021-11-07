new_list = []   # создаем пустой список

for i in range(1, 1000, 2):
    new_list.append(i ** 3)  # добавляем в него кубы нечетных чисел от 1 до 1000

total = 0  # создаем переменную, в которую запишем сумму цифр нужных нам чисел
sum_number = 0  # создаем переменную, в которую запишем сумму цифр от числа
for number in new_list:
    while number != 0:
        sum_number = sum_number + number % 10
        number = number // 10
        if sum_number % 7 != 0:   # если есть остаток от деления, то идем дальше
            continue
        else:    # нужное нам число записываем в тотал
            total = total + sum_number
print(total)

total = 0  # создаем переменную, в которую запишем сумму цифр нужных нам чисел
sum_number = 0  # создаем переменную, в которую запишем сумму цифр от числа
for number in new_list:
    number = number + 17   # выполняем второе условие
    while number != 0:
        sum_number = sum_number + number % 10
        number = number // 10
        if sum_number % 7 != 0:   # если есть остаток от деления, то идем дальше
            continue
        else:    # нужное нам число записываем в тотал
            total = total + sum_number
print(total)
