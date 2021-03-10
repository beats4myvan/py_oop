# from encapsulation.football_team_generator.team import Team


class Player:
    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    def __str__(self):
        return f'Player: {self.name}\n' \
               f'Endurance: {self.endurance}\n' \
               f'Sprint: {self.sprint}\n' \
               f'Dribble: {self.dribble}\n' \
               f'Passing: {self.passing}\n' \
               f'Shooting: {self.shooting}\n'


# player_1 = Player("p1", 5, 10, 2, 5, 6)
# player_2 = Player("p2", 5, 10, 2, 1, 1)
#
# t = Team('Levski', 5)
# print(t.add_player(player_1))
# print(t.add_player(player_1))
# print(t.remove_player(player_1))