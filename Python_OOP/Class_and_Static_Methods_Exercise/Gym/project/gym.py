from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self) -> None:
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan) -> None:
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription) -> None:
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription_ = [s.__repr__() for s in self.subscriptions if s.id == subscription_id][0]
        customer_ = [c.__repr__() for c in self.customers if c.id == subscription_id][0]
        trainer_ = [t.__repr__() for t in self.trainers if t.id == subscription_id][0]
        equipment_ = [e.__repr__() for e in self.equipment if e.id == subscription_id][0]
        plan_ = [p.__repr__() for p in self.plans if p.id == subscription_id][0]

        return f"{subscription_}\n{customer_}\n{trainer_}\n{equipment_}\n{plan_}"
