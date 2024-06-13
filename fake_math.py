def divide(first, second):
    if second == 0:
        print('Ошибка')
    else:
        print(round((first / second), 2))


if __name__ == '__main__':
    divide(23, 3)
