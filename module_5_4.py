class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        print(cls.houses_history)
        return object.__new__(cls)

    def __init__(self, name, numberOfFloors):
        self.numberOfFloors = numberOfFloors
        self.name = name


    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')


house_1 = House("Дом № 1", 10)
house_2 = House("Дом № 2", 6)
house_3 = House("Дом № 3", 9)
