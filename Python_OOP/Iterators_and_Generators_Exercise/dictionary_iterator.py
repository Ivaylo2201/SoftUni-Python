class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict = dict_obj
        self.length = len(self.dict)
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start >= self.length:
            raise StopIteration

        return list(self.dict.items())[self.start]


result = dictionary_iter({1: "1", 2: "2"})

for x in result:
    print(x)
