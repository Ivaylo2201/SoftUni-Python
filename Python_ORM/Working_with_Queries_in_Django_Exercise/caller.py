import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries

from main_app.models import ChessPlayer, Meal, Dungeon, Workout, ArtworkGallery, Laptop


def show_highest_rated_art() -> str:
    art = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{art.art_name} is the highest-rated art with {art.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([
        first_art, second_art
    ])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(
        rating__lt=0
    ).delete()


# LAPTOPS

def show_the_most_expensive_laptop() -> str:
    laptop = Laptop.objects.order_by('-price', 'id').first()
    return f"{laptop.brand} is the most expensive laptop available for {laptop.price}$!"


def bulk_create_laptops(*args) -> None:
    Laptop.objects.bulk_create(
        *args
    )


def update_to_512_GB_storage() -> None:
    Laptop.objects.filter(brand__in=[
        "Asus", "Lenovo"
    ]).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=[
        "Apple", "Dell", "Acer"
    ]).update(memory=16)


def update_operation_systems() -> None:
    OS_UPDATE: dict = {
        "Asus": "Windows",
        "Apple": "MacOS",
        "Dell": "Linux",
        "Acer": "Linux",
        "Lenovo": "Chrome OS"
    }

    for laptop in Laptop.objects.all():
        laptop.operation_system = OS_UPDATE[laptop.brand]
        laptop.save()


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(
        price__lt=1200
    ).delete()


#
# # CHESS PLAYER
#
#
def bulk_create_chess_players(*args) -> None:
    ChessPlayer.objects.bulk_create(
        *args
    )


def delete_chess_players() -> None:
    ChessPlayer.objects.filter(
        title='no title'
    ).delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(
        title='GM'
    ).update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(
        title='no title'
    ).update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(
        rating__gte=2400
    ).update(title='GM')


def grand_chess_title_IM() -> None:
    ChessPlayer.objects.filter(
        rating__range=[2300, 2399]
    ).update(title='IM')


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(
        rating__range=[2200, 2299]
    ).update(title='FM')


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(
        rating__range=[0, 2199]
    ).update(title='regular player')


#
# # MEAL
#
MEALS: dict = {
    "Breakfast": ["Gordon Ramsay", "10 minutes"],
    "Lunch": ["Julia Child", "12 minutes"],
    "Dinner": ["Jamie Oliver", "15 minutes"],
    "Snack": ["Thomas Keller", "5 minutes"]
}


def set_new_chefs() -> None:
    for meal in Meal.objects.all():
        meal.chef = MEALS[meal.meal_type][0]
        meal.save()


def set_new_preparation_times() -> None:
    for meal in Meal.objects.all():
        meal.preparation_time = MEALS[meal.meal_type][1]
        meal.save()


def update_low_calorie_meals() -> None:
    Meal.objects.filter(
        meal_type__in=['Breakfast', 'Dinner']
    ).update(calories=400)


def update_high_calorie_meals() -> None:
    Meal.objects.filter(
        meal_type__in=['Lunch', 'Snack']
    ).update(calories=700)


def delete_lunch_and_snack_meals() -> None:
    Meal.objects.filter(
        meal_type__in=['Lunch', 'Snack']
    ).delete()


#
# # DUNGEON
#
DUNGEON_NAMES: dict = {
    "Easy": ["The Erased Thombs", 25, "Enchanted Maze"],
    "Medium": ["The Coral Labyrinth", 50, "Grimstone Mines"],
    "Hard": ["The Lost Haunt", 75, "Shadowed Abyss"]
}


def show_hard_dungeons() -> str:
    return '\n'.join(
        f"{d.name} is guarded by {d.boss_name} who has {d.boss_health} health points!"
        for d in Dungeon.objects
        .filter(difficulty='Hard')
        .order_by('-location')
    )


def bulk_create_dungeons(*args) -> None:
    Dungeon.objects.bulk_create(*args)


def update_dungeon_names() -> None:
    Dungeon.objects.filter(difficulty="Easy").update(name="The Erased Thombs")
    Dungeon.objects.filter(difficulty="Medium").update(name="The Coral Labyrinth")
    Dungeon.objects.filter(difficulty="Hard").update(name="The Lost Haunt")


def update_dungeon_bosses_health() -> None:
    (Dungeon.objects
     .exclude(difficulty="Easy")
     .update(boss_health=500))


def update_dungeon_recommended_levels() -> None:
    Dungeon.objects.filter(difficulty="Easy").update(recommended_level=25)
    Dungeon.objects.filter(difficulty="Medium").update(recommended_level=50)
    Dungeon.objects.filter(difficulty="Hard").update(recommended_level=75)


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(boss_health=500).update(reward="1000 Gold")
    Dungeon.objects.filter(location__startswith="E").update(reward="New dungeon unlocked")
    Dungeon.objects.filter(location__endswith="S").update(reward="Dragonheart Amulet")


def set_new_locations() -> None:
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


def show_workouts() -> str:
    return '\n'.join(
        f"{w.name} from {w.workout_type} type has {w.difficulty} difficulty!"
        for w in Workout.objects
        .filter(workout_type__in=["Calisthenics", "CrossFit"])
    )


def get_high_difficulty_cardio_workouts() -> QuerySet[Workout]:
    return (Workout.objects
            .filter(workout_type="Cardio", difficulty="High")
            .order_by("instructor"))


def set_new_instructors() -> None:
    Workout.objects.filter(workout_type="Cardio").update(instructor="John Smith")
    Workout.objects.filter(workout_type="Strength").update(instructor="Michael Williams")
    Workout.objects.filter(workout_type="Yoga").update(instructor="Emily Johnson")
    Workout.objects.filter(workout_type="CrossFit").update(instructor="Sarah Davis")
    Workout.objects.filter(workout_type="Calisthenics").update(instructor="Chris Heria")


def set_new_duration_times() -> None:
    Workout.objects.filter(instructor="John Smith").update(duration="15 minutes")
    Workout.objects.filter(instructor="Sarah Davis").update(duration="30 minutes")
    Workout.objects.filter(instructor="Chris Heria").update(duration="45 minutes")
    Workout.objects.filter(instructor="Michael Williams").update(duration="1 hour")
    Workout.objects.filter(instructor="Emily Johnson").update(duration="1 hour and 30 minutes")


def delete_workouts() -> None:
    (Workout.objects
     .exclude(workout_type__in=["Strength", "Calisthenics"])
     .delete())



