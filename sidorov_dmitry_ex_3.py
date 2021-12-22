import copy

def tutors_to_classes(list1, list2):
    """Генератор выводит кортежи (list1, list2), сделанные по копиям поданных в него
    списков с добавлением None при необходимости"""
    list1_copy = copy.deepcopy(list1)  # делаем копию через дипкопи
    list2_copy = copy.deepcopy(list2)
    if len(list1_copy) > len(list2_copy):
        for _ in range(len(list1_copy - list2_copy)):   # циклом добавляем None до нужной нам длины
            list2_copy.append(None)
    for t, k in zip(list1_copy, list2_copy):    # генератор с кортежами через цикл с использованием zip
        yield t, k

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
print(tutors_to_classes(tutors, klasses))
