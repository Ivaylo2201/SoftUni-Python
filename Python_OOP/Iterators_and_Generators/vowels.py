class vowels:
    def __init__(self, text: str) -> None:
        self.text = text
        self.vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.idx += 1

        try:
            if self.text[self.idx].lower() in self.vowels:
                return self.text[self.idx]
            # Searching for the next vowel since we don't want to print the consonants
            return self.__next__()

        except IndexError:
            raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
