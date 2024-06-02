import random


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

def get_matrix_2(nn, mm, vv):
    matrix_2 = []
    for i in range(nn):
        matrix_2.append([])
        for j in range(mm):
            vv = random.randint(0, 100)
            matrix_2[i].append(vv)
    print(matrix_2)


nn = int(input('введите количество повторений в списке: '))
mm = int(input('введите длину внутреннего списка: '))
vv = random.randint(0, 100)
get_matrix_2(nn, mm, vv)
