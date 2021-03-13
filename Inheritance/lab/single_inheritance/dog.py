from zoo.animal import Animal


class Dog(Animal):
    def bark(self):
        return 'barking'


animal = Animal()
print(animal.eat())

dog = Dog()
print(dog.bark())
print(dog.eat())
