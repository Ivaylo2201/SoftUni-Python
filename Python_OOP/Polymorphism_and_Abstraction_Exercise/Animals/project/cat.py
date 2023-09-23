from project.animal import Animal


class Cat(Animal):
    def __repr__(self) -> str:
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"

    def make_sound(self) -> str:
        return "Meow meow!"
