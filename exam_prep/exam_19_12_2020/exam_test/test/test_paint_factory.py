from project.factory.paint_factory import PaintFactory

import unittest


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PaintFactory("Test", 5)

    def test_paint_factory_init__expect_correct_attributes(self):
        self.assertEqual("Test", self.factory.name)
        self.assertEqual(5, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)

    def test_paint_factory_add_ingredient__when_not_valid_ingredients_type__expect_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.factory.add_ingredient("test", 2)

        self.assertEqual(f"Ingredient of type test not allowed in PaintFactory", str(context.exception))

    def test_capacity_of_factory(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient('green', 200)
        self.assertEqual('Not enough space in factory', str(ex.exception))

    def test_capacity_error(self):
        with self.assertRaises(ValueError):
            self.factory.add_ingredient('green', 2222)

    def test_remove_error(self):
        self.factory.add_ingredient('green', 2)
        with self.assertRaises(ValueError):
            self.factory.remove_ingredient('green', 9999)

    def test_remove4_error(self):
        with self.assertRaises(KeyError):
            self.factory.remove_ingredient('green', 9999)

    def test_ingredient_remove(self):
        self.factory.add_ingredient('white', 2)
        self.factory.remove_ingredient('white', 1)
        self.assertEqual({'white': 1}, self.factory.ingredients)

    def test_paint_factory_product_prop__expect_to_return_ingredients(self):
        self.assertEqual({}, self.factory.products)

    def test_add_ingredient(self):
        self.factory.add_ingredient('white', 2)
        self.assertEqual({'white': 2}, self.factory.ingredients)

    # def test_paint_factory_add_ingredient__when_ingredient_in_ingredients__expect_to_addition(self):
    #     self.factory.add_ingredient("white", 2)
    #     self.factory.add_ingredient("white", 2)
    #     self.assertEqual({"white": 4}, self.factory.ingredients)


if __name__ == '__main__':
    unittest.main()
