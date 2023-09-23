class Equipment:
    id = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.id = Equipment.get_next_id()

    @staticmethod
    def get_next_id() -> int:
        Equipment.id += 1
        return Equipment.id

    def __repr__(self) -> str:
        return f"Equipment <{self.id}> {self.name}"
