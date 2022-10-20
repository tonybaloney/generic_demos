from statistics import median as std_median


def median(values: list[int] | list[float]) -> float | int:
    return std_median(values) # or some other calculation

m = median([1, 2, 3])  # float | int

from typing import TypeVar

TNumber = TypeVar("TNumber", float, int)

def median2(values: list[TNumber]) -> TNumber:
    return std_median(values) # or some other calculation

m = median2([1, 2, 3])  # int
