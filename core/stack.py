from typing import List, Tuple


class FifthStack:
    def __init__(self):
        self._data: List[int] = []
        self._copy: List[int] = []

    def __str__(self):
        return str(self._data)

    def push(self, item: int) -> None:
        self._data.append(item)

    def pop(self) -> int:
        return self._data.pop()

    def pop2(self) -> Tuple[int, int]:
        item1 = self._data.pop()
        item2 = self._data.pop()
        return (item1, item2)

    def save_snapshot(self):
        self._copy = self._data.copy()

    def rollback(self):
        self._data = self._copy.copy()
