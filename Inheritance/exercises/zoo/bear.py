from zoo.mammal import Mammal


class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)


# mammal = Mammal("Stella")
# print(mammal.__class__.__bases__[0].__name__)
# print(mammal.name)
# print(mammal._Animal__name)
# lizard = Lizard("John")
# print(lizard.__class__.__bases__[0].__name__)
# print(lizard.name)
# print(lizard._Animal__name)
