import unittest

from testing.test_cat import Cat


class CatTests(unittest.TestCase):
    name = 'Edi'

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_fed_after_eat(self):
        # Cat is fed after eating
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cannot_sleep_if_not_fed(self):
        self.cat.fed = False
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
