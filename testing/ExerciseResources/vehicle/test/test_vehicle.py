import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    fuel = 50
    capacity = 60
    horse_power = 100
    fuel_consumption = 1.25

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_drive_exception_raise(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(999)
        self.assertEqual('Not enough fuel', str(context.exception))

    def test_can_drive_the_frollowin_kilometeres(self):
        drive_kilometers = 1
        self.vehicle.drive(drive_kilometers)
        self.assertEqual(48.75, self.vehicle.fuel)

    def test_refuel_exeption(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(999)
        self.assertEqual('Too much fuel', str(context.exception))

    def test__str_repr(self):
        expected = f"The vehicle has {self.horse_power} horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"
        actual = self.vehicle.__str__()
        self.assertEqual(expected, actual)

    def test_fuel_after_drive(self):
        kilometers = 2
        self.vehicle.drive(kilometers)
        actual_result = 47.5
        fuel_needed = self.fuel_consumption * kilometers
        fuel_left = self.fuel - fuel_needed
        self.assertEqual(fuel_left, actual_result)

    def test_refuel_sum(self):
        expected_fuel = 52
        fuel = 2
        self.vehicle.capacity = 60
        self.vehicle.refuel(fuel)
        self.assertEqual(expected_fuel, self.vehicle.fuel)


if __name__ == '__main__':
    unittest.main()
