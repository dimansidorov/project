list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_2 = []
for element in list_1:
    if element.isdigit():
        list_2.extend(['"', f'{int(element):02}', '"'])
    elif (element.startswith('+') or element.startswith('-')) and element[1:].isdigit():
        list_2.extend(['"', f'{element[0]} {int(element[1:]):02}', '"'])
    else:
        list_2.append(element)

print(' '.join(list_2))
