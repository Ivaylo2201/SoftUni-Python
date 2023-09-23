from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        pass


class Car(Vehicle):
    AIR_CONDITIONER_EXPENSE = 0.9

    def drive(self, distance: int) -> None:
        used_fuel = distance * (self.fuel_consumption + Car.AIR_CONDITIONER_EXPENSE)

        if self.fuel_quantity >= used_fuel:
            self.fuel_quantity -= used_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_EXPENSE = 1.6
    TANK_HOLE_EXPENSE = 0.95

    def drive(self, distance: int) -> None:
        used_fuel = distance * (self.fuel_consumption + Truck.AIR_CONDITIONER_EXPENSE)

        if self.fuel_quantity >= used_fuel:
            self.fuel_quantity -= used_fuel

    def refuel(self, fuel: int) -> None:
        self.fuel_quantity += fuel * Truck.TANK_HOLE_EXPENSE


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
