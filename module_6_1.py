class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

    def eat(self):
        if self.edible == True:
            print(f'{self.name} - съедобное')
        else: print(f'{self.name} - несъедобное')


class Mammal(Animal):

    def eat(self, food):
        self.food = Plant.edible
        if food == True:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Predator(Animal):

    def eat(self, food):
        self.food = Plant.edible
        if food == True:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(Plant.eat(p1))
print(Plant.eat(p2))


print(a1.name)
print(p1.name)

print(f'{a1.name} - живой: {a1.alive}')
print(f'{a2.name} - сытый: {a2.fed}')
a1.eat(p1)
a2.eat(p2)
print(f'{a1.name} - живой: {a1.alive}')
print(f'{a2.name} - сытый: {a2.fed}')

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
