from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def make_sound(self) -> str:
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += Owl.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    def make_sound(self) -> str:
        return "Cluck"

    def feed(self, food):
        self.weight += Hen.WEIGHT_INCREASE * food.quantity
        self.food_eaten += food.quantity
