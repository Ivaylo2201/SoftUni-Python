from typing import List, Union

from Encapsulation_Exercise.Wild_Cat_Zoo.project.caretaker import Caretaker
from Encapsulation_Exercise.Wild_Cat_Zoo.project.cheetah import Cheetah
from Encapsulation_Exercise.Wild_Cat_Zoo.project.keeper import Keeper
from Encapsulation_Exercise.Wild_Cat_Zoo.project.lion import Lion
from Encapsulation_Exercise.Wild_Cat_Zoo.project.tiger import Tiger
from Encapsulation_Exercise.Wild_Cat_Zoo.project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Union[Lion, Tiger, Cheetah]] = []
        self.workers: List[Union[Keeper, Caretaker, Vet]] = []

    def add_animal(self, animal: Union[Lion, Tiger, Cheetah], price: int) -> str:
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"

        elif self.__budget < price:
            return "Not enough budget"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Union[Keeper, Caretaker, Vet]) -> str:
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum([w.salary for w in self.workers])

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_care_money = sum([a.money_for_care for a in self.animals])

        if self.__budget >= total_care_money:
            self.__budget -= total_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = [l for l in self.animals if isinstance(l, Lion)]
        tigers = [t for t in self.animals if isinstance(t, Tiger)]
        cheetahs = [c for c in self.animals if isinstance(c, Cheetah)]
        animals_info: List[str] = []
        result = f"You have {len(self.animals)} animals\n"

        animals_info.append(f"----- {len(lions)} Lions:")
        for l in lions:
            animals_info.append(f"{l.__repr__()}")

        animals_info.append(f"----- {len(tigers)} Tigers:")
        for t in tigers:
            animals_info.append(f"{t.__repr__()}")

        animals_info.append(f"----- {len(cheetahs)} Cheetahs:")
        for c in cheetahs:
            animals_info.append(f"{c.__repr__()}")

        return result + "\n".join(animals_info)

    def workers_status(self) -> str:
        keepers = [k for k in self.workers if isinstance(k, Keeper)]
        caretakers = [c for c in self.workers if isinstance(c, Caretaker)]
        vets = [v for v in self.workers if isinstance(v, Vet)]
        workers_info = []
        result = f"You have {len(self.workers)} workers\n"

        workers_info.append(f"----- {len(keepers)} Keepers:")
        for l in keepers:
            workers_info.append(f"{l.__repr__()}")

        workers_info.append(f"----- {len(caretakers)} Caretakers:")
        for t in caretakers:
            workers_info.append(f"{t.__repr__()}")

        workers_info.append(f"----- {len(vets)} Vets:")
        for c in vets:
            workers_info.append(f"{c.__repr__()}")

        return result + "\n".join(workers_info)
