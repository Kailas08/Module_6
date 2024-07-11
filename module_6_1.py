class  Animal: # Родительский класс "Животных"

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.alive = True
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
            self.fed = False

class Plant: #Родительский класс "Растений"

    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal): # Класс млекопитающих, дочерний класс "животных"
    def __init__(self, name):
        super().__init__(name)

class Predator(Animal): # Класс хищников, дочерний класс "животных"
    def __init__(self, name):
        super().__init__(name)

class Flower(Plant): # Класс "цветы", дочернийкласс "растений"
    def __init__(self, name):
        super().__init__(name)



class Fruit(Plant): # Класс "фрукты", дочерний класса "растений"

    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Волк с Уол-Стрит')
a2 = Mammal('Шимпанзе')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print('Кормим волка')
a1.eat(p1)
print(a1.alive)
print(a1.fed)

print('Кормим шимпанзе')
a2.eat(p2)
print(a2.alive)
print(a2.fed)
