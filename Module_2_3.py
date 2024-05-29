my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
my_list_new = ["a", "b"]
while a <= (len(my_list)-1):
    number = my_list[a]
    if number > 0:
        print(number)
        a = a + 1
        my_list_new.append(number)
    else:
        a = a + 1
print('Числовой ряд закончился')
my_list_new.remove("a")
my_list_new.remove("b")
print(my_list_new)
