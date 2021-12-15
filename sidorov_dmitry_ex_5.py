import random


def get_jokes(num, repeat=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []  # список, в котором будем хранить шутки
    if num > 5:
        num = 5
        print('Максимальное число шуток пять :)')
    a, b, c = nouns[:], adverbs[:], adjectives[:]  # создаем копии списков
    if repeat:  # если задаем повтор
        for i in range(num):
            random.shuffle(a), random.shuffle(b), random.shuffle(c)
            joke_list.append(f'{a[i]} {b[i]} {c[i]}')
    else:  # не нужен повтор
        for i in range(num):
            random.shuffle(a), random.shuffle(b), random.shuffle(c)
            joke_list.append(f'{a[0]} {b[0]} {c[0]}')
            del a[0]  # удаляем из копии список
            del b[0]
            del c[0]
    return joke_list


n = int(input())
print(get_jokes(n, repeat=True))
print(get_jokes(n, repeat=False))
