class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return f'This pokemon is already caught'
        else:
            self.pokemon.append(pokemon)
            self.name = pokemon
            return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        if pokemon_name in self.name:
            self.pokemon.remove(pokemon_name)
            return f' Ypu have released {pokemon_name}'
        else:
            return f'Pokemon is Not  caught'

    def trainer_data(self):
        return f'pokemon Trainer {self.name}\n' \
               f'Pokemon count {len(self.pokemon)}\n' \
               f'{self.pokemon}'


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
