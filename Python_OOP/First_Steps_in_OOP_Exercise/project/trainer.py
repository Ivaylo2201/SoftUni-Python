from First_Steps_in_OOP_Exercise.project.pokemon import Pokemon
from typing import List


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon_name: Pokemon) -> str:
        if pokemon_name not in self.pokemons:
            self.pokemons.append(pokemon_name)
            return f"Caught {pokemon_name.pokemon_details()}"

        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"

        return f"Pokemon is not caught"

    def trainer_data(self) -> str:
        pokemons_data = '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemons])

        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{pokemons_data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
