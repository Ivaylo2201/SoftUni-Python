from project.room import Room
from typing import List


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        for r in self.rooms:
            if r.number == room_number and not r.is_taken:
                if not r.take_room(people):
                    self.guests += people
                return None

    def free_room(self, room_number: int) -> None:
        for r in self.rooms:
            if r.number == room_number and r.is_taken:
                guests = r.guests
                if not r.free_room:
                    self.guests -= guests
                return None

    def status(self) -> str:
        free_rooms: List[str] = []
        taken_rooms: List[str] = []

        for r in self.rooms:
            if not r.is_taken:
                free_rooms.append(str(r.number))
            else:
                taken_rooms.append(str(r.number))

        result = [f"Hotel {self.name} has {self.guests} total guests", f"Free rooms: {', '.join(free_rooms)}", f"Taken rooms: {', '.join(taken_rooms)}"]
        return '\n'.join(result)


hotel = Hotel.from_stars(5)
first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)
hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)
hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)
print(hotel.status())
