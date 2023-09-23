from typing import List


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other):
        total_people = []
        total_people.extend(self.people)
        total_people.extend(other.people)

        return Group(f"{self.name} {other.name}", total_people)

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join([f'{p.name} {p.surname}' for p in self.people])}"

    def __getitem__(self, item) -> str:
        return f"Person {item}: {self.people[item].name} {self.people[item].surname}"

    def __iter__(self) -> str:
        for index, p in enumerate(self.people):
            yield f"Person {index}: {p.name} {p.surname}"
