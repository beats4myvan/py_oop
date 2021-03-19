# class Animal:
#     pass


class Dog:
    sound = 'woof'

    def get_sound(self):
        return self.sound


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())
        # if animal.species == 'cat':
        #     print('meow')
        # elif animal.species == 'dog':
        #     print('woof-woof')
        # elif animal.species == 'chicken':
        #     print('chicken')


# animals = [Animal('cat'), Animal('dog')]
animals = [Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се
# правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
