import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    name = "edi"
    type = "cow"
    sound = "Myyyy"

    def setUp(self):
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_mamal_name_type_sound(self):
        expected_name = 'edi'
        expected_type = 'cow'
        expected_sound = 'Myyyy'
        self.assertEqual(expected_sound, self.mammal.sound)
        self.assertEqual(expected_type, self.mammal.type)
        self.assertEqual(expected_name, self.mammal.name)

    def test_mammal_kingdom_initial(self):
        mammal = Mammal(self.name, self.type, self.sound)
        result = mammal._Mammal__kingdom
        expected_result = "animals"
        self.assertEqual(result, expected_result)

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom_name(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info_returned(self):
        self.assertEqual(f'{self.mammal.name} is of type {self.mammal.type}', self.mammal.info())


if __name__ == '__main__':
    unittest.main()
