from typing import Generic, TypeVar

V = TypeVar('V')

class ValueMessage(Generic[V]):
    def __init__(self, value: V | None, message: str | None = None):
        self.value = value
        self.message = message