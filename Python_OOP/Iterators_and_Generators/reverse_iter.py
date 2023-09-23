class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start -= 1

        try:
            return self.iterable[self.start]
        except IndexError:
            raise StopIteration


p = reverse_iter([1, 2, 3, 4, 5])
for i in p:
    print(i)
