from Encapsulation_Exercise.Wild_Cat_Zoo.project.animal import Animal


class Tiger(Animal):
    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, money_for_care=45)
