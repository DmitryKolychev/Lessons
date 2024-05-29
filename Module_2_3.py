my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a <= (len(my_list)-1):
    number = my_list[a]
    if number > 0:
        print(number)
        a = a + 1
        continue
    else:
        a = a + 1
print('Числовой ряд закончился')
