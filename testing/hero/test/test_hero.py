from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = 'MadMax'
    health = 100
    damage = 5
    level = 5

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_hero_init_method_attributes(self):
        self.assertEqual('MadMax', self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_battle_exception_test(self):
        with self.assertRaises(Exception) as context:
            enemy_hero = self.hero
            self.hero.battle(enemy_hero)

        self.assertEqual('You cannot fight yourself', str(context.exception))

    def test_battle_exception_if_hero_lower_health(self):
        with self.assertRaises(Exception) as context:
            self.hero.health = 0
            enemy_hero = Hero('Hero', 5, 100, 3)
            self.hero.battle(enemy_hero)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(context.exception))

    def test_battle_exception_if_enemy_hero_has_lower_health(self):
        with self.assertRaises(Exception) as context:
            enemy_hero = Hero('Enemy Hero Pesho', 5, 0, 3)
            self.hero.battle(enemy_hero)

        self.assertEqual(f'You cannot fight {enemy_hero.username}. He needs to rest', str(context.exception))

    def test_battle_results(self):
        enemy_hero = Hero('Enemy Hero Pesho', 5, 100, 3)
        self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.health, 85)
        self.assertEqual(enemy_hero.health, 80)

    def test_you_win_if__healt_0(self):
        enemy_hero = Hero('Enemy Hero Pesho', 5, 10, 3)
        expected_message = 'You win'
        actual_message = self.hero.battle(enemy_hero)
        self.assertEqual(expected_message, actual_message)

    def test_you_loose_if_self_health_under_0(self):
        enemy_hero = Hero('Enemy Hero Pesho', 50, 110, 30)
        expected_message = 'You lose'
        actual_message = self.hero.battle(enemy_hero)
        self.assertEqual(expected_message, actual_message)

    def test__rerp_method(self):
        expected = f"Hero MadMax: 5 lvl\n" \
                   f"Health: 100\n" \
                   f"Damage: 5\n"
        actual_result = self.hero.__str__()

        self.assertEqual(expected, actual_result)

    def test_if_health_of_both_hero_is_0(self):
        enemy_hero = Hero('Enemy Hero Pesho', 50, 1, 30)
        expected_result = 'Draw'
        result = self.hero.battle(enemy_hero)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    main()
