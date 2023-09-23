from typing import Sequence


class sequence_repeat:
    def __init__(self, sequence: Sequence, number: int):
        self.sequence = sequence
        self.number = number
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        self.number -= 1

        if self.start >= len(self.sequence):
            self.start = 0

        if self.number < 0 or self.start >= len(self.sequence):
            raise StopIteration

        return self.sequence[self.start]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
