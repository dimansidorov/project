import sys
import json

d = {}      # создаем словарь
with open('users.csv', 'r', encoding='utf-8') as file1, \
        open('hobby.csv', 'r', encoding='utf-8') as file2:
    for row_pt1 in file1:       # row_pt1 - первая часть(фио), pt2 - хобби
        row_pt2 = file2.readline().strip()
        if not row_pt2:     # если второй части нет - None
            row_pt2 = None
        if row_pt1 not in d:
            d[row_pt1.strip()] = row_pt2
    if file2.read():
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as res_f:   # записываем в финальный файл
    msg = json.dumps(d, ensure_ascii=False)
    res_f.write(msg)
with open('result.json', 'r', encoding='utf-8') as res_f:   # читаем его
    result = json.loads(res_f.read())
print(result)   # выводим результат







