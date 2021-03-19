from wild_farm.animals import Bird
from wild_farm.animals.mammals import Mouse

from Polymorphism_and_magic_methods.exercise.wild_farm.food import Meat

class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.get_weight_food_eaten(self.WEIGHT_INCREASE, food)


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        return self.get_weight_food_eaten(self.WEIGHT_INCREASE, food)

# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)

#
# hen = Hen("Harry", 10, 10)
mouse = Mouse("vanka", 0.5, "maze")
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(mouse)
print(mouse.make_sound())
mouse.feed(veg)
mouse.feed(fruit)

print(mouse.feed(meat))
print(mouse)
#
