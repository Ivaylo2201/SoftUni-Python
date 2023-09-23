from project.food import Vegetable, Fruit, Meat
from project.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    def make_sound(self) -> str:
        return "Squeak"

    def feed(self, food) -> None or str:
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += Mouse.WEIGHT_INCREASE * food.quantity
            self.food_eaten += food.quantity
            return None

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    def make_sound(self) -> str:
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Dog.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    def make_sound(self) -> str:
        return "Meow"

    def feed(self, food) -> None or str:
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.weight += Cat.WEIGHT_INCREASE * food.quantity
            self.food_eaten += food.quantity
            return None

        return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    WEIGHT_INCREASE = 1

    def make_sound(self) -> str:
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Tiger.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
