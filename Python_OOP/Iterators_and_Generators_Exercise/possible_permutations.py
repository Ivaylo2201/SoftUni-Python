from itertools import permutations


def possible_permutations(sequence):
    for el in permutations(sequence):
        yield list(el)