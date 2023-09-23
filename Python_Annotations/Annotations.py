from typing import Any, Final, Iterable, Sequence, Callable

# 'var' is considered a constant and should not be reassigned (An error won't be thrown if we change it)
VAR: Final[int] = 1
VARSTR: Final[str] = 'hello'


def function_any(var: Any) -> None:
    # 'var' can be of any type
    ...


def function_iterable(some_set: Iterable[int]) -> None:
    # An iterable is a collection you can iterate over. DISCLAIMER: It can be unordered!

    # Iterable[int] = [1, 2, 3]
    # Iterable[str, int] = {"one": 1, "two": 2}
    # Iterable[float] = (1.00, 2.50, 3.75)
    # Iterable[str] = {"a", "b", "c"}

    ...


def function_sequence(some_list: Sequence[int]) -> None:
    # A sequence is an ORDERED collection you can iterate over.
    # Every sequence is an iterable

    # Sequence[int] = [1, 2, 3]
    # Sequence[str, int] = {"one": 1, "two": 2}
    # Sequence[float] = (1.00, 2.50, 3.75)

    # Sets can't be used as a sequence since they are an unordered collection

    ...


def function_optional(var: None | int) -> None:
    # Old way: var: Optional[int]
    ...


def function_union(var: str | int) -> None:
    # Old way: var: Union[str, int]
    ...


def function_callable(f: Callable[[int, str], None]) -> None:
    # 'f' is a function that accepts an int and a string as arguments and returns None
    ...
