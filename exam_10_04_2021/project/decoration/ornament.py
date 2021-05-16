from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):
    ornament_comfort = 1
    ornament_price = 5

    def __init__(self):
        super().__init__(Ornament.ornament_comfort, Ornament.ornament_price)
