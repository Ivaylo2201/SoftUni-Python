from typing import List


class Stack:
    """At the stop"""

    # gdfgdf

    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        if isinstance(element, str):
            self.data.append(element)

    def pop(self) -> str:
        element = self.data[-1]
        self.data.remove(element)
        return element

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return True if not self.data else False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"
