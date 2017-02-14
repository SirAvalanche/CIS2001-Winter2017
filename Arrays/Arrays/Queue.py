class Queue(object):
    """description of class"""

    def __init__(self):
        self._storage = []
        self._front = 0

    def __len__(self):
        return len(self._storage)

    def enqueue(self, obj):
        self._storage.append(obj)

    def dequeue(self):
        return self._storage.pop(0)

    def front(self):
        return self._storage[0]
