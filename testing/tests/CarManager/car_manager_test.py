import unittest

from testing.CarManager.car_manager import Car


class CarTest(unittest.TestCase):
    make = 'make'
    model = 'model'
    fuel_consumption = 10
    fuel_capacity = 100

    def setUp(self):
        self.car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_car_make_setter__when_None__expect_exception(self):
        # car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception) as context:
            self.car.make = None

        self.assertEqual('Make cannot be null or empty!', str(context.exception))

    def test_car_refuel__when_provided_fuel_is_0__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_car_refuel__when_provided_fuel_is_negative__expect_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-1)

    def test_car_refuel__when_provided_fuel_is_correct__expect_to_increase_fuel_amount_by_provided_fuel(self):
        fuel = 50
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, fuel)

    def test_car_refuel__when_provided_fuel_is_more_than_fuel_capacity__expect_to_increase_fuel_amount_to_fuel_capacity(
            self):
        fuel = 124
        self.car.refuel(fuel)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_car_model_setter__when_None__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.model = None

        self.assertEqual('Model cannot be null or empty!', str(context.exception))

    def test_car_fuel_consumption(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(context.exception))

    def test_car_fuel_capacity(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(context.exception))

    def test_car_fuel_amount(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1

        self.assertEqual('Fuel amount cannot be negative!', str(context.exception))

    def test__exception_can_drive_whit_provided_fuel(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(999)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_drive_fuel_decrease(self):
        self.car.fuel_amount = 999
        self.car.drive(10)
        self.assertEqual(998, self.car.fuel_amount)

if __name__ == '__main__':
    unittest.main()
