import os

ROOT = './'    # папка с содержимым
os.chdir('some_data')   # переходим в папку some_data

result = {0: 0, 10: 0, 100: 0, 1000: 0, 10000: 0, 100000: 0, 1000000: 0}  # создаем словарь
a = [key for key in result.keys()]  # создаем список с ключами для перебора по циклу
for _root, _dirs, files in os.walk('.'):
    for file in files:      # цикл по файлам
        sz = os.stat(file).st_size          # берем размер файла
        for i in range(len(a)):     # проходим по ключам списка
            if sz < a[i]:
                result[a[i]] = result.get(a[i], 0) + 1
                break
            elif sz > a[i]:
                continue
            elif sz > a[-1]:    # создаем условие, которое сообщает нам, что файл слишком большой, если такой есть
                print(f'Слишком большой файл по условию задачи: {file}, Размер: {sz}')
print(result)
