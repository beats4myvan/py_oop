from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, drive, refuel):
        self.drive = drive
        self.refuel = refuel

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(self.drive, self.refuel)
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        air_condition = 0.9
        fuel_needed = (self.fuel_consumption + air_condition) * distance
        if self.fuel_quantity > fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(self.drive, self.refuel)
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        air_condition = 1.6
        fuel_needed = (self.fuel_consumption + air_condition) * distance
        if self.fuel_quantity > fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        hole_in_fuel_tank = 0.95
        self.fuel_quantity += fuel * hole_in_fuel_tank
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
