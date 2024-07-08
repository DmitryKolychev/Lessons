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
            return
        else:
            print(f'{self.name} - несъедобное')
        return


class Mammal(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            self.alive = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            self.fed = False


class Predator(Animal):

    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
            self.alive = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            self.fed = False


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

Plant.eat(p1)
Plant.eat(p2)

print(a1.name)
print(p1.name)

print(f'{a1.name} - живой: {a1.alive}')
print(f'{a2.name} - сытый: {a2.fed}')
print()
a1.eat(p1)
print(f'{a1.name} - живой: {a1.alive} и сытый: {a1.fed}')
print()
a2.eat(p2)
print(f'{a2.name} - живой: {a2.alive} и сытый: {a2.fed}')
print()
a1.eat(p2)
print(f'{a1.name} - живой: {a1.alive} и сытый: {a1.fed}')
print()
a2.eat(p1)
print(f'{a2.name} - живой: {a2.alive} и сытый: {a2.fed}')
# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
