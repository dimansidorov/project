import os  # импортируем модуль os

dir_name = 'my_project'  # даем имя основной папке
if not os.path.exists(dir_name):  # если такой папки нет - создаем
    os.mkdir(dir_name)
paths = [os.path.join(dir_name, 'settings'), os.path.join(dir_name, 'mainapp'), os.path.join(dir_name, 'adminapp'),
         os.path.join(dir_name, 'authapp')]  # создаем список с папками, которые необходимо будет вложить
for path in paths:  # при помощи цикла создаем
    if not os.path.exists(path):
        os.makedirs(path)
