from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    def calculate_comfort(self):
        '''Returns the sum of each decoration’s comfort in the Aquarium'''
        return sum([item.comfort for item in self.decorations])

    def add_fish(self, fish):
        if self.__valid_fish_type(fish):
            if len(self.fish) < self.capacity:
                # add fish
                self.fish.append(fish)
                return f'"Successfully added {fish.__class__.__name__} to {self.name}'
            return f'Not enough capacity.'

    def __valid_fish_type(self, fish):
        fish_types = ['FreshwaterFish', 'SaltwaterFish']
        if fish.__class__.__name__ in fish_types:
            return True
        return False

    def remove_fish(self, fish):
        '''Removes a fish object from the Aquarium.'''
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        '''The feed() method feeds all fish in the aquarium.'''
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\nFish: {' '.join(f.name for f in self.fish) if self.fish else 'none'}\n" \
                 f"Decorations: {len(self.decorations)}\nComfort: {self.calculate_comfort()}\n"
        return result
