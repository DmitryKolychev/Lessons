my_dict = {'Dima': 1982, 'Misha': 2006, 'Ivan': 1994}
print(my_dict)
print(my_dict.keys())
Name=input('Введите имя из списка:')
print("Год рождения данного участника:" , my_dict[Name])
Name2=input('Введите имя не из списка: ')
print("Проверка в списке наличие участника по имени", Name2, ":", my_dict.get(Name2, "совпадений не найдено"))
my_dict.update({'Julia': 1999, 'Masha': 2004})
print(my_dict)
a = my_dict.pop('Dima')
del my_dict['Ivan']
print(my_dict)
print(a)
my_set = {1, 2, 'a', 'b', 'c', 'a', 1, 3, 'b', 1.1, 2.5, False}
print(my_set)
my_set.update({5, 'C'})
print(my_set)
my_set.discard(1.1)
print(my_set)