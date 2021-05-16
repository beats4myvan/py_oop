from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    plant_comfort = 5
    plant_price = 10

    def __init__(self):
        super().__init__(Plant.plant_comfort, Plant.plant_price)
