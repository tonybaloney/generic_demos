from typing import Sequence, TypeVar

T = TypeVar("T")

def first(values: Sequence[T], default: T) -> T:
    if len(values) == 0:
        return default
    return values[0]

names = ["Harry", "Barry", "Warry"]

first_name = first(names, "Jarry") # str
