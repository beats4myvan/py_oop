
class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player: Player):
        if not player.name in self.list_of_players and player.guild == 'Unaffiliated':
            self.list_of_players.append(player.name)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {player.guild}"
        elif player.guild == self.name:
            return f'Player {player.name} is already in the guild.'
        elif player.guild != self.name:
            return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str):
        if player_name in self.list_of_players:
            self.list_of_players.remove(player_name)
            player.guild = 'Unaffiliated'
            return f'Player {player_name} has been removed from the guild.'
        else:
            return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        return f'Guild: {player.guild}\n{player.player_info()}'


