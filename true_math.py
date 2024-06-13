def divide(first, second):
    if second == 0:
        from math import inf
        print(inf)
        return inf
    else:
        print(round((first / second), 2))


if __name__ == '__main__':
    a = divide(10, 0)
    print(a)
