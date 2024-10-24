class Animal:
    def __init__(self, name: str):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name: str):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def eat(self, food: Plant):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Animal):
    def eat(self, food: Plant):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):
    def __init__(self, name: str):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name: str):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк')
a2 = Mammal('Овца')
p1 = Flower('Цветок')
p2 = Fruit('Фрукт')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
