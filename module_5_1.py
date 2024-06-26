class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def go_to(self):
        new_floor = int(input(f"Какой этаж Вас интересует в {self.name}? "))
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i + 1)
        else:
            print('Такого этажа не существует')


house_1 = House('Vidnoe', 5)
house_2 = House('Pavshino', 16)
print(house_1.name, house_1.number_of_floors)
print(house_2.name, house_2.number_of_floors)
house_1.go_to()
house_2.go_to()
house_3 = House(input(f'Введите название ЖК: '), int(input(f'Введите количество этажей: ')))
house_3.go_to()
