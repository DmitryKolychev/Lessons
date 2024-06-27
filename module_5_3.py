from time import sleep
from os import system


class Building:
    def __init__(self, name, floors, b_type):
        self.buildingName = name
        self.numberOfFloors = floors
        self.buildingType = b_type

    def __eq__(self, other):
        # return self is other
        return (self.numberOfFloors is other.numberOfFloors and self.buildingType is other.buidingType)  # and
        # self.buildingName is other.buildingName)

    def __lt__(self, other):
        return self.numberOfFloors < other.numberOfFloors

    def __gt__(self, other):
        return self.numberOfFloors > other.numberOfFloors

    def __sub__(self, other):
        return self.numberOfFloors - other.numberOfFloors

    def __ne__(self, other):
        return self.buildingType != other.buildingType


def height_material():
    if (spisok[b_1].numberOfFloors is spisok[b_2].numberOfFloors and
        spisok[b_1].buildingType is spisok[b_2].buildingType) == False:
        print(f'{spisok[b_1].buildingName} не идентичен {spisok[b_2].buildingName}')
        # высота
        if spisok[b_1] < spisok[b_2]:
            print(f'{spisok[b_1].buildingName} ниже, чем {spisok[b_2].buildingName}')
        elif spisok[b_1] > spisok[b_2]:
            print(f'{spisok[b_1].buildingName} выше, чем {spisok[b_2].buildingName}')
        else:
            print(f'{spisok[b_1].buildingName} и {spisok[b_2].buildingName} одинаковой высоты')
        # материал
        if spisok[b_1].buildingType != spisok[b_2].buildingType:
            print(f'Материал {spisok[b_1].buildingName} и {spisok[b_2].buildingName} не одинаковый: '
                  f'{spisok[b_1].buildingType} и {spisok[b_2].buildingType} соответственно.')
        else:
            print(f'{spisok[b_1].buildingName} и {spisok[b_2].buildingName} построены из одинакового материала:'
                  f'  {spisok[b_1].buildingType}.')
    else:
        print(f'{spisok[b_1].buildingName} и {spisok[b_2].buildingName} идентичны.')


building_1 = Building('"Пирамида_1"', 10, "кирпич")
building_2 = Building('"Вилла_1"', 3, "кирпич")
building_3 = Building('"Пирамида_2"', 10, "бетон")
building_4 = Building('"Вилла_2"', 3, "бетон")
building_5 = Building('"Пирамида_3"', 10, "кирпич")

spisok = {1: building_1, 2: building_2, 3: building_3, 4: building_4, 5: building_5}

i = 0
while i in range(5):
    i += 1
    print(f'1: {building_1.buildingName}, 2: {building_2.buildingName}, '
          f'3: {building_3.buildingName}, 4: {building_4.buildingName}, 5: {building_5.buildingName}')

    b_1 = int(input("Укажите номер 1-го здания для сравнения: "))
    b_2 = int(input("Укажите номер 2-го здания для сравнения: "))
    print()
    print(f'Вы выбрали {spisok[b_1].buildingName} и {spisok[b_2].buildingName}')
    height_material()
    print(f'Сравните сами \n'
          f'{spisok[b_1].buildingName}: этажей {spisok[b_1].numberOfFloors}, материал: {spisok[b_1].buildingType} \n'
          f'{spisok[b_2].buildingName}: этажей {spisok[b_2].numberOfFloors}, материал: {spisok[b_2].buildingType} ')
    print()
    sleep(5)
    system('cls') # не работает :(

