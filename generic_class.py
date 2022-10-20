from datetime import datetime
from typing import TypeVar, Generic
from uuid import UUID

TKey = TypeVar("TKey", int, UUID)
TValue = TypeVar("TValue")

class Record(Generic[TKey, TValue]):
    created: datetime
    key: TKey
    value: TValue

    def __init__(self, key: TKey, value: TValue):
        self.key = key
        self.value = value
    
    def update(self, value: TValue):
        self.value = value

record1 = Record(1, "Hello") # Record[int, str]
record1.update("new word") # update(value: str)
record1.update(1)  # typing error.
