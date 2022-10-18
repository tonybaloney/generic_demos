from datetime import datetime
from typing import Any, List, Tuple, TypeVar, Generic, TypeVarTuple
from uuid import UUID

TKey = TypeVar("TKey", int, UUID)
TValues = TypeVarTuple("TValues")

class Record(Generic[TKey, *TValues]):
    created: datetime
    key: TKey
    values: Tuple[*TValues]

    def __init__(self, key: TKey, *values: *TValues):
        self.key = key
        self.values = values
    
    def update(self, *values: *TValues):
        self.values = values

record1 = Record(1, "Hello", 12.3, 1234)
record1.update("new word", 123., 32343)

a, b, c = record1.values


