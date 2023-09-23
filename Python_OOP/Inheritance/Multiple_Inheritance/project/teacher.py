from Wild_Cat_Zoo.project import Employee
from Wild_Cat_Zoo.project import Person


class Teacher(Person, Employee):
    @staticmethod
    def teach() -> str:
        return "teaching..."
