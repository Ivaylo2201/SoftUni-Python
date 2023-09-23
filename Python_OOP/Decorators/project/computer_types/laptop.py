from project.computer_types.computer import Computer
from math import log


class Laptop(Computer):
    def configure_computer(self, processor: str, ram: int) -> str:
        available_processors = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }
        valid_ram_sizes = [2, 4, 8, 16, 32, 64]

        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with laptop"
                             f" {self.manufacturer} {self.model}!")

        if ram not in valid_ram_sizes:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop"
                             f" {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = available_processors[processor] + int(log(ram, 2) * 100)

        return f"Created {self.manufacturer} {self.model} with {self.processor}" \
               f" and {self.ram}GB RAM for {self.price}$."
