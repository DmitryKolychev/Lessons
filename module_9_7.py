import random
def is_prime(func):
    def wrapper(*args):
        i = func(*args)
        k = i - 1
        if i < 2:
            return f"{i} -не простое, не составное"
        for k in range(i):
            try:
                 if i % k == 0 and k > 1:
                     return f'{i} - составное число'
            except ZeroDivisionError:
                 ('ноль')
        return f'{i} - простое число'
    return wrapper

@is_prime
def sum_three(*args):
    a = sum(args)
    return a


result = sum_three(2, 3, 6)
print(result)
rnd = tuple(random.randint(0, 20) for _ in range(3))
result2 = sum_three(*rnd)
print(rnd)
print(result2)