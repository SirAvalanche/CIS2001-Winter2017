from ArrayListBase import ArrayListBase

class Stack():
    """description of class"""

    def __init__(self):
        self._storage = []

    def __len__(self):
        return len(self._storage)

    def pop(self):
        return self._storage.pop()

    def push(self, obj):
        self._storage.append(obj)

    def top(self):
        if len(self._storage) == 0:
            raise IndexError("Stack is emtpy!")
        return self._storage[len(self._storage) - 1]
