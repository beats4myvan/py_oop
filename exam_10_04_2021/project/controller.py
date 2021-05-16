from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = []
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        valid_decors = ['Ornament', 'Plant']
        if decoration_type in valid_decors:
            self.decorations_repository.append(decoration_type)
            return f'Successfully added {decoration_type}.'
        return f'Invalid decoration type.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        if aquarium_name in self.aquariums and decoration_type in self.decorations_repository:
            aquarium_to_find = [aq for aq in self.aquariums if aq.name == aquarium_name][0]
            aquarium_to_find.add_decoration(decoration_type)
            self.decorations_repository.remove(decoration_type)

            return f'Successfully added {decoration_type} to {aquarium_name}.'
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == 'SaltwaterFish':
            fish = SaltwaterFish(fish_name, fish_species, price)
            for i in self.aquariums:
                if i == aquarium_name:
                    return i.add(fish)
        elif fish_type == 'FreshwaterFish':
            fish = FreshwaterFish(fish_name, fish_species, price)
            for i in self.aquariums:
                if i == aquarium_name:
                    return i.add(fish)

        return f"There isn't a fish of type {fish_type}"

    def feed_fish(self, aquarium_name):
        aquarium_to_find = [aq for aq in self.aquariums if aq.name == aquarium_name][0]
        aquarium_to_find.feed()
        return f"Fish fed: {len(aquarium_to_find.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium_to_find = [aq for aq in self.aquariums if aq.name == aquarium_name][0]
        aquarium_to_find_sum = sum(d for d in aquarium_to_find.decorations)
        return f"The value of Aquarium {aquarium_name} is {aquarium_to_find_sum:.2f}."

    def report(self):
        a_results = [str(a) for a in self.aquariums]
        return '\n'.join(a_results)
