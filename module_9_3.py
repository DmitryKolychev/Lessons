first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер', 'Компьютер']

zp = zip(first, second)
first_result = (abs(len(x) - len(y)) for x, y in zp if len(x) != len(y))

second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
# min(len(first), len(second)) - определяет какой список короче
print(list(first_result))
print(list(second_result))

