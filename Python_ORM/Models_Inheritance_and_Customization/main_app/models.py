from django.core.exceptions import ValidationError
from django.db import models
from datetime import date


# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Its fur color is {self.fur_color}."


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f"Its wingspan is {self.wing_span} cm."


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    class Specializations(models.TextChoices):
        Mammals = "Mammals"
        Birds = "Birds"
        Reptiles = "Reptiles"
        Others = "Others"

    specialty = models.CharField(max_length=10, choices=Specializations.choices)
    managed_animals = models.ManyToManyField(to=Animal)

    def clean(self):
        super().clean()  # When is this invoked?

        if self.specialty not in self.Specializations:
            raise ValidationError("Specialty must be a valid choice.")

class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs['choices'] = [
            (True, 'Available'),
            (False, 'Not Available')
        ]
        kwargs['default'] = True

        super().__init__(*args, **kwargs)

class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)
    availability = BooleanChoiceField()

    def is_available(self) -> bool:
        return self.availability


class ZooDisplayAnimal(Animal):
    # Use the class Animal when we don't have access to it
    # ZooDisplayAnimal acts like Animal

    def __extra_info(self) -> str:
        if hasattr(self, 'mammal'):
            return f" Its fur color is {self.mammal.fur_color}."
        elif hasattr(self, 'bird'):
            return f" Its wingspan is {self.bird.wing_span} cm."
        elif hasattr(self, 'reptile'):
            return f" Its scale type is {self.reptile.scale_type}."
        else:
            return ''

    def display_info(self) -> str:
        return (f"Meet {self.name}! It's {self.species} and it's born {self.birth_date}."
                f" It makes a noise like '{self.sound}'!{self.__extra_info()}")

    def is_endangered(self) -> bool:
        ENDANGERED_SPECIES: list = [
            "Cross River Gorilla", "Orangutan", "Green Turtle"
        ]
        return self.species in ENDANGERED_SPECIES

    class Meta:
        proxy = True
