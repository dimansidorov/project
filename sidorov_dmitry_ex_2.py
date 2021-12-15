def num_translate_adv(word):  # создаем функцию, которая возвращает значение из словаря
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
    if word[0].isupper():
        word = word.lower()
        return eng_rus_dict[word].capitalize()
    if word[0].lower():
        return eng_rus_dict[word].lower()
    if word not in eng_rus_dict:
        return None


word = input()  # запрашиваем у пользователя слово. которое необходимо перевести
print(num_translate_adv(word))  # вывод функции
