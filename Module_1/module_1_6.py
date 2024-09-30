my_dict={'Ivan': 1986, 'Semen':1992, 'Irina':1998}
print('Словарь: ', my_dict)
print('Год Ивана: ', my_dict['Ivan'])
print('Поиск несуществующего значения: ', my_dict.get('Alena'))
my_dict['Anton'] = 1982
my_dict.update({'Nikolay': 1995})
print('Удаленная запись: ', my_dict.pop('Semen'))
print('Измененный словарь: ', my_dict)
print()
my_set={'Стол', 5, 3.14, 7, 3.14, (2, 4, 6, 8, 0), 5, 'Стол'}
print('Множество: ', my_set)
my_set.add(33)
my_set.add('Стул')
my_set.discard(7)
print('Измененное множество: ', my_set)