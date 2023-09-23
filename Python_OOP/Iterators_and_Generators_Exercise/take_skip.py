class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.start = 0 - self.step
        self.curr_iter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        self.curr_iter += 1

        if self.curr_iter > self.count:
            raise StopIteration
        return self.start
