from wizard import Wizard
from elf import Elf
from hero import Hero
from players_and_monsters.dark_knight import DarkKnight

class BladeKnight(DarkKnight):
    def __init__(self, username, level):
        super().__init__(username, level)


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
wizard3 = Wizard("w", 4)
print(str(elf))
print(wizard3.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)