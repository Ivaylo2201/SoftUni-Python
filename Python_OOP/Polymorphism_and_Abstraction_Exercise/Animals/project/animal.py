from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def make_sound(self) -> str:
        pass
