from project.dvd import DVD
from typing import List


class Customer:
    def __init__(self, name: str, age: int, customer_id: int) -> None:
        self.name = name
        self.age = age
        self.id = customer_id
        self.rented_dvds: List[DVD] = []

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({', '.join([d.name for d in self.rented_dvds])})"
