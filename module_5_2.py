class House:
    def __init__(self, name, numberOfFloors):
        self.name = name
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self):
        self.floor = input('Введите новое количество этажей: ')
        self.numberOfFloors = self.floor


house_1 = House("Дом № 1", 0)
print(f'{house_1.name}, количество этажей: {house_1.numberOfFloors}')
house_1.setNewNumberOfFloors()
print(f'{house_1.name}, уточнённое количество этажей: {house_1.numberOfFloors}')
print()
house_2 = House("Дом № 2", 0)
print(f'{house_2.name}, количество этажей: {house_2.numberOfFloors}')
house_2.setNewNumberOfFloors()
print(f'{house_2.name}, уточнённое количество этажей: {house_2.numberOfFloors}')
