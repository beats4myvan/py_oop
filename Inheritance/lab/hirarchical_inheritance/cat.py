from zoo.animal import Animal
from animals.dog import Dog
class Cat(Animal):
    def meow(self):
        return 'meowking..'

animal = Animal()
print(animal.eat())

dog = Dog()
print(dog.bark())
print(dog.eat())

cat = Cat()
print(cat.meow())
print(cat.eat())