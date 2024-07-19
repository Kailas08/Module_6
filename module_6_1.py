class  Animal: # Родительский класс "Животных"
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            Animal.alive = False
            Animal.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            Animal.alive = True
            Animal.fed = False
            print(f'{self.name} не стал есть {food.name}')
class Plant: #Родительский класс "Растений"
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal): # Класс млекопитающих, дочерний класс "животных"
    pass

class Predator(Animal): # Класс хищников, дочерний класс "животных"
    pass

class Flower(Plant): # Класс "цветы", дочернийкласс "растений"
    pass

class Fruit(Plant): # Класс "фрукты", дочерний класса "растений"
    edible = True
    pass



a1 = Predator('Волк с Уол-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print('Кормим волка')
a1.eat(p1)
print(a1.alive)
print(a1.fed)

print('Кормим Хатико')
a2.eat(p2)
print(a2.alive)
print(a2.fed)
