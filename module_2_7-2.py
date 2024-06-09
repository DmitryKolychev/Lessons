number = input('Введите число: ')
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(number)
print(f"Произведение всех цифр из числа =  {result}")

while result > 0:
    number = input('Введите число: ')
    get_multiplied_digits(number)
    result = get_multiplied_digits(number)
    print(f"Произведение всех цифр из числа =  {result}")