import unittest

from project.train.train import Train


class TestCaseBase(unittest.TestCase):
    def assertListEmpty(self, ll):
        self.assertListEqual([], ll)


class TestTrain(unittest.TestCase):
    TRAIN_FULL = "Train is full"
    PASSENGER_EXISTS = "Passenger {} Exists"
    PASSENGER_NOT_FOUND = "Passenger Not Found"
    PASSENGER_ADD = "Added passenger {}"
    PASSENGER_REMOVED = "Removed {}"
    ZERO_CAPACITY = 0

    def setUp(self):
        self.train = Train('BDJ', 2)
        self.passengers = []

    def test__init__when_all_valid__expect_be_set(self):
        self.assertEqual(self.TRAIN_FULL, "Train is full")
        self.assertEqual(self.PASSENGER_EXISTS, "Passenger {} Exists")
        self.assertEqual(self.PASSENGER_NOT_FOUND, "Passenger Not Found")

    def test_remove_passanger(self):
        with self.assertRaises(ValueError) as context:
            self.train.remove('Georgi')
        self.assertEqual('Passenger Not Found', str(context.exception))

    def test_add_passanger(self):
        self.passengers = ['Georgi']
        with self.assertRaises(ValueError) as context:
            self.train.add('Georgi')
            self.train.add('Georgi')
        self.assertEqual('Passenger Georgi Exists', str(context.exception))

    def test_add_more_passanger(self):
        self.passengers = ['Georgi']
        with self.assertRaises(ValueError) as context:
            self.train.add('Georgi')
            self.train.add('PEtar')
            self.train.add('Ivan')
        self.assertEqual('Train is full', str(context.exception))

    def test_pass_removed(self):
        self.assertEqual(self.passengers, [])

    def test_passanger_removed(self):
        self.assertEqual('Added passenger ge', self.train.add("ge"))

    def test_passanger_removed_true(self):
        self.train.add('Georgi')
        self.assertEqual('Removed Georgi', self.train.remove('Georgi'))


if __name__ == '__main__':
    unittest.main()
