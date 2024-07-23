import math


class Figure:
    sides_count = 0

    def __init__(self, sides, color, filled=True):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return (isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print(f'Цвет для {self.__class__.__name__} не может быть изменён.\n'
                  f'Неверное указано значение. Необходимо вводить целые числа от 0 до 255 включительно.')

    def __is_valid_sides(self, *sides):
        if (all((isinstance(i, int) and i > 0) for i in sides)):
            return len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        else:
            print(f'Вы ввели неверное количество сторон для {self.__class__.__name__}.')

    def __len__(self):
        if self.sides_count == 1:
            return self.side
        else:
            return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        super().__init__(side, color)
        self.side = side
        self.__radius = self.side / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, s1, s2, s3, filled=True):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        super().__init__([s1, s2, s3], color, filled)

    def calculate_height(self):
        p = (self.s1 + self.s2 + self.s3) / 2
        self.__height = (2 * math.sqrt(p * (p - self.s1) * (p - self.s2) * (p - self.s3))) / self.s1
        return self.__height


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length, filled=True):
        super().__init__([side_length] * Cube.sides_count, color, filled)
        self.side_length = side_length

    def get_volume(self):
        return self.side_length ** 3


# Пример использования
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
tr = Triangle((10, 200, 50), 6, 10, 15)

# # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(f'Значения RGB у {circle1.__class__.__name__} {circle1.get_color()}')
cube1.set_color(300, 70, 15)  # Не изменится
print(f'Значения RGB у {cube1.__class__.__name__} {cube1.get_color()}')

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
tr.set_sides(10, 15, 20)
print(tr.get_sides())

# Проверка периметра (круга), это и есть длина:
print(f'Периметр {circle1.__class__.__name__} =  {len(circle1)}')

# Проверка периметра (треугольника):
print(f'Периметр {tr.__class__.__name__} =  {len(tr)}')

# Проверка периметра (куба):
print(f'Периметр {circle1.__class__.__name__} =  {len(cube1)}')

# Проверка объёма (куба):
print(f'Объём {circle1.__class__.__name__} составляет {cube1.get_volume():.1f}')
# Проверка объёма (треугольника):
print(f'Высота у {tr.__class__.__name__} = {tr.calculate_height():.1f}')
print(f'Значения RGB у {tr.__class__.__name__} {tr.get_color()}')
