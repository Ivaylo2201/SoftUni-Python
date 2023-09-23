from project.player import Player
from typing import List


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str:
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> Player or str:
        for p in self.__players:
            if p.name == player_name:
                self.__players.remove(p)
                return p

        return f"Player {player_name} not found"

