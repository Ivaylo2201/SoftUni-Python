from Wild_Cat_Zoo.project import Product


class Drink(Product):
    def __init__(self, name: str):
        super().__init__(name, 10)
