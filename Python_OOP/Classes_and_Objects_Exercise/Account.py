from typing import Union


class Account:
    def __init__(self, account_id: int, name: str, balance: int = 0):
        self.id = account_id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> Union[int, str]:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance

        return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"
