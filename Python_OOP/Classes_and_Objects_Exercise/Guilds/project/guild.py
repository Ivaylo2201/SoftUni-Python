from Wild_Cat_Zoo.project import Player
from typing import List


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, n_player: Player) -> str:
        if n_player.guild == self.name:
            return f"Player {n_player.name} is already in the guild."

        elif n_player.guild != "Unaffiliated":
            return f"Player {n_player.name} is in another guild."

        self.players.append(n_player)
        n_player.guild = self.name

        return f"Welcome player {n_player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        for n_player in self.players:
            if n_player.name == player_name:
                n_player.guild = "Unaffiliated"
                self.players.remove(n_player)

                return f"Player {n_player.name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        players_info = '\n'.join([f'{n_player.player_info()}' for n_player in self.players])
        return f"Guild: {self.name}\n{players_info}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
