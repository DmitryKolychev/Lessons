numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 26, 25, 23, 41, 27, 43,
           24]  # после 15 добавил числа не по возрастанию
primes = numbers[1:]
not_primes = []
for i in numbers[1:]:
    for j in numbers[1:]:
        if i == j:
            continue
        k = i % j
        if k == 0:
            not_primes.append(i)
            primes.remove(i)
            break
print('числовой ряд:', numbers)
print('простые числа:', sorted(primes))
print('НЕпростые числа:', sorted(not_primes))
