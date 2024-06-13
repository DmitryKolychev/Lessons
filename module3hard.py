data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
data_structure2 = [
    {'a': 4, 'b': 5}, (8, 5, [9, 5, 4]),
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    summa = 0
    for i in args:
        if isinstance(i, int):
            summa += i
        elif isinstance(i, str):
            summa += len(i)
        elif isinstance(i, (tuple, list, set)):
            summa += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            summa += calculate_structure_sum(*i.items())
    return summa


result = calculate_structure_sum(data_structure)
print(f'Сумма всех числе: {result}')


def bukva_structure_sum(*args):
    summa2 = 0
    for i in args:
        if isinstance(i, str):
            summa2 += len(i)
        elif isinstance(i, (tuple, list, set)):
            summa2 += bukva_structure_sum(*i)
        elif isinstance(i, dict):
            summa2 += bukva_structure_sum(*i.items())
    return summa2


result2 = bukva_structure_sum(data_structure)
print(f'Сумма всех букв (и чисел, сохранненых как буквы): {result2}')


def structure_sum(*args):
    _List = 0
    for i in args:
        if isinstance(i, list):
            _List += 1
            _List += structure_sum(*i)
        elif isinstance(i, (set, tuple)):
            _List += structure_sum(*i)
            if isinstance(i, list):
                _List += 1

    return _List


def structure_sum2(*args):
    _Tuple = 0
    for i in args:
        if isinstance(i, (set, list)):
            _Tuple += structure_sum2(*i)
            if isinstance(i, tuple):
                _Tuple += 1
        elif isinstance(i, tuple):
            _Tuple += 1
            _Tuple += structure_sum2(*i)

    return _Tuple


def structure_sum3(*args):
    _Set = 0
    for i in args:
        if isinstance(i, (tuple, list)):
            _Set += structure_sum2(*i)
            if isinstance(i, set):
                _Set += 1
        elif isinstance(i, set):
            _Set += 1
            _Set += structure_sum2(*i)

    return _Set


def structure_sum4(*args):
    _Dict = 0
    for i in args:
        if isinstance(i, dict):
            _Dict += 1
        elif isinstance(i, (tuple, list, set)):
            _Dict += structure_sum2(*i)
            if isinstance(i, dict):
                _Dict += 1

    return _Dict


result3 = structure_sum(data_structure2)
result4 = structure_sum2(data_structure2)
result5 = structure_sum3(data_structure2)
result6 = structure_sum4(data_structure2)
print(data_structure2)
print(f'количество списков []: {result3}')
print(f'количество кортежов (): {result4}')
print(f'количество множеств : {result5}')
print(f'количество словарей : {result6}')
