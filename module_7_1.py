from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        with open(Shop.__file_name, 'r') as file:
            return file.read()

    def add(self, *products):
        new_products = self.get_products().splitlines()
        new_names = {line.split(', ')[0] for line in new_products}
        for product in products:
            if product.name not in new_names:
                file = open(Shop.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

# Вывод на консоль:
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
