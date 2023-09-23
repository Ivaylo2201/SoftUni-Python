from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop
from typing import List, Union


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[Union[DesktopComputer, Laptop]] = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int) -> str:
        valid_type_computers = {
            "Desktop Computer": DesktopComputer,
            "Laptop": Laptop
        }

        if type_computer not in valid_type_computers:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = valid_type_computers[type_computer](manufacturer, model)
        message = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for c in self.warehouse:
            if c.price <= client_budget and c.processor == wanted_processor and c.ram >= wanted_ram:
                profit = client_budget - c.price
                self.profits += profit
                self.warehouse.remove(c)
                return f"{c.__repr__()} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
