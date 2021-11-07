# реализовать вывод информации времени в удобном формате
# используем if
duration = int(input('Введите колличество секунд для конвертации '))

if duration < 60 : #вариант, если у нас нет целых минут
    print(duration, 'Секунд')
elif duration >=60 and duration <  3600: # вариант, если есть целые минуты
    min = duration // 60
    sec = duration % 60
    print(min, 'минут', sec, 'секунд')
elif duration >= 3600 and duration < 86400 :  # вариант, если есть целые часы
    hour = duration // 3600
    min = (duration % 3600) //60
    sec = duration % 3600 % 60
    print(hour, 'часов', min, 'минут', sec, 'секунд')
#elif duration >= 86400 : # вариант, если есть целые часы через elif
else: #тоже самое, только тут нет нужды прописывать условия
    day = duration // 86400
    hour = duration % 86400// 3600
    min = duration % 86400 % 3600 // 60
    sec = duration % 86400 % 3600 % 60
    print(day, 'дней', hour, 'часов', min, 'минут', sec, 'секунд')
