from typing import Generic, TypeVar

V = TypeVar('V')
E = TypeVar('E', bound=Exception)

class ValueException(Generic[V, E]):
    def __init__(self, value: V | None, exception: E | None = None):
        self.value = value
        self.exception = exception