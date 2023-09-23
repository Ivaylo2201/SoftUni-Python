class custom_range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
        self.current = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration
        return self.current
