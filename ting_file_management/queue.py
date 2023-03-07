from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def enqueue(self, value):
        return self._items.append(value)

    def dequeue(self):
        if not self._items:
            raise ValueError("Queue is empty")
        return self._items.pop(0)

    def search(self, index):
        if not 0 <= index < len(self._items):
            raise IndexError("Index out of bounds")
        return self._items[index]
