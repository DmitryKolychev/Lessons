
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)




print_params(b=25)
print_params()
print_params(c = [1,2,3])

print()
values_list = ['word', True, 27.89]
print_params(*values_list)
print()
values_dict = {'a': "Фамилия", 'b': 'Имя', 'c': 'Отчество'}
print_params(**values_dict)
print()
values_list_2 = [25.34, 'good']
print_params(*values_list_2, 'без С')