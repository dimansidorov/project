def num_translate(word):  # создаем функцию, которая возвращает значение из словаря
    eng_rus_dict = {'zero': 'ноль',  # создаем словарь
                    'one': 'один',
                    'two': 'два',
                    'three': 'три',
                    'four': 'четыре',
                    'five': 'пять',
                    'six': 'шесть',
                    'seven': 'семь',
                    'eight': 'восемь',
                    'nine': 'девять',
                    'ten': 'десять'
                    }
    if word in eng_rus_dict:
        return eng_rus_dict[word]
    else:
        return None


word = input()  # запрашиваем у пользователя слово. которое необходимо перевести
print(num_translate(word))  # вывод функции
