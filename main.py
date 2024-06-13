from fake_math import divide as fm
from true_math import divide as tm


def delenie(first, second):
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    if second == 0:
        sposob = input('Введите "ш" если хотите выбрать школьную программу,' + '\n' +
                       'введите "в" если хотите выбрать высшую математику: ')
        if sposob.lower() in ('ш', 'i'):
            fm(first, second)
            print()
        elif sposob.lower() in ('в', 'd'):
            tm(first, second)
            print()
        else:
            print('Вы ввели неверную букву' + '\n') 
            return
    else:
        fm(first, second)
        print()


n = 10  # количество циклов
for i in range(n):
    delenie(63, 3)
    if (n - i - 1) == 0:
        break
    print(f'Осталось циклов: {n - i - 1}')
    stop = input('Если хотите остановить цикл, нажмите "c"' + '\n' + 'для продолжения нажмите любую кнопку: ')
    if stop.lower() in ('c', 'с'):
        break
    else:
        print()
        continue
