from abc import ABC, abstractmethod


class Medicine(ABC):
    @abstractmethod
    def __init__(self, health_increase):
        self.health_increase = health_increase

    @property
    def health_increase(self):
        return self._health_increase

    @health_increase.setter
    def health_increase(self, value):
        if value < 0:
            raise ValueError("Health increase cannot be less than zero.")
        self._health_increase = value

    # @staticmethod
    # def test_health_increase_is_bigger_than_0(value):
    #     if value < 0:
    #         raise ValueError('Health increase cannot be less than zero.')

    def apply(self, survivor):
        ##Method should increase the health property of the given survivor with the medicine's health_increase value
        survivor.health += self.health_increase
