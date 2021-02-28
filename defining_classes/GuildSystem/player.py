class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if not skill_name in self.skills:
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        else:
            return f'Skill already added"'


    def player_info(self):
        result = f'Name: {self.name}\nGuild: {self.guild}\n' \
                 f'HP: {self.hp}\nMP: {self.mp}\n' \
                 f''
        for skill, mana in self.skills.items():
            result += f'==={skill} - {mana}\n'
            return result

