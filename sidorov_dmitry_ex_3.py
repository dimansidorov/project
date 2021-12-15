def thesaurus(*names):
    names_dict = {}
    for name in names:
        key = name[0]
        if key in names_dict:
            names_dict[key].append(name)
        else:
            names_dict[key] = []
            names_dict[key].append(name)
    return names_dict


employee = ('Дмитрий', 'София', 'Даниил', 'Татьяна', 'Ольга', 'Оксана')
print(thesaurus(*employee))
