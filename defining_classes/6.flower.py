class Flower:
    def __init__(self, name, water_requirements, is_happy=False):
        self.water_requirements = water_requirements
        self.name = name
        self.is_happy = is_happy

    def status(self):
        if self.is_happy:
            return f'{self.name} is happy'
        else:
            return f'{self.name} is not happy'

    def water(self, quntity):
        # if quntity >= self.water_requirements:
        #     self.is_happy = True
        self.is_happy = quntity >= self.water_requirements


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(100)
print(flower.status())
