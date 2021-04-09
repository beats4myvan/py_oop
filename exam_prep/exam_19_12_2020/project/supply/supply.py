from abc import ABC, abstractmethod

from project.survivor import Survivor


class Supply(ABC):
    @abstractmethod
    def __init__(self, needs_increase):
        self.needs_increase = needs_increase

    def apply(self, survivor):
        ##Method should increase the needs property of the given survivor with the supply's needs_increase value
        survivor.needs += self.needs_increase

    @property
    def needs_increase(self):
        return self._needs_increase

    @needs_increase.setter
    def needs_increase(self, value):
        if value < 0:
            raise ValueError("Needs increase cannot be less than zero.")
        self._needs_increase = value

    # @staticmethod
    # def test_need_increase_not_zero(value):
    #     if value < 0:
    #         raise ValueError("Needs increase cannot be less than zero.")
