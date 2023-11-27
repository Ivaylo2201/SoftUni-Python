import os
import django
from datetime import date

from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str) -> str:
    Pet.objects.create(name=name, species=species)

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    Artifact.objects.create(
        name=name, origin=origin, age=age,
        description=description, is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations() -> str:
    return '\n'.join([
        f"{loc.name} has a population of {loc.population}!"
        for loc in Location.objects.all().order_by('-id')
    ])


def new_capital() -> None:
    loc = Location.objects.first()
    loc.is_capital = True
    loc.save()


def get_capitals() -> QuerySet:
    return Location.objects.filter(
        is_capital=True
    ).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount() -> None:
    for car in Car.objects.all():
        discount: int = sum([int(x) for x in str(car.year)])
        car.price_with_discount = float(car.price) - float(car.price) * (discount / 100)

        car.save()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(
        year__gt=2020
    ).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks() -> str:
    return '\n'.join(
        [f"Task - {task.title} needs to be done until {task.due_date}!"
         for task in Task.objects.filter(is_finished=False)]
    )


def complete_odd_tasks() -> None:
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str) -> None:
    replacement: str = ''.join([chr(ord(ch) - 3) for ch in text])

    for task in Task.objects.all():
        if task.title == task_title:
            task.description = replacement
            task.save()


def get_deluxe_rooms() -> str:
    return '\n'.join(
        [f"Deluxe room with number {room.room_number} costs {room.price_per_night}$ per night!"
         for room in HotelRoom.objects.filter(room_type='Deluxe') if room.id % 2 == 0]
    )


def increase_room_capacity() -> None:
    rooms = HotelRoom.objects.all().order_by('id')
    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            continue
        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity
        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()
