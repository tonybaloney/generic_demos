from typing import Any, Sequence


def first(values: Sequence, default: Any) -> Any:
    if len(values) == 0:
        return default
    return values[0]

names = ["Harry", "Barry", "Warry"] # list[str]

first_name = first(names, "Jarry") # first_name=Any
