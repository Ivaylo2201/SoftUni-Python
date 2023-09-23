from Wild_Cat_Zoo.project import Product
from Wild_Cat_Zoo.project import Food
from Wild_Cat_Zoo.project import Drink
from typing import List


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name: str) -> None:
        p = self.find(product_name)
        self.products.remove(p)

    def __repr__(self) -> str:
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
