from project.computer_types.computer import Computer
from math import log


class DesktopComputer(Computer):
    def configure_computer(self, processor: str, ram: int) -> str:
        available_processors = {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }
        valid_ram_sizes = [2, 4, 8, 16, 32, 64, 128]

        if processor not in available_processors:
            raise ValueError(f"{processor} is not compatible with desktop computer"
                             f" {self.manufacturer} {self.model}!")

        if ram not in valid_ram_sizes:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer"
                             f" {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = available_processors[processor] + int((log(ram, 2) * 100))

        return f"Created {self.manufacturer} {self.model} with {self.processor}" \
               f" and {self.ram}GB RAM for {self.price}$."
