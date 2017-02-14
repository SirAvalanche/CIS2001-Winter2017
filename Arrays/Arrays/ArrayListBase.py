import ctypes

class ArrayListBase(object):
    """Custom implemenation of an 'array' backed list"""

    def __init__(self, capacity=1):
        self._size = 0
        if capacity <= 0:
            capacity = 1
        self._capacity = capacity
        self._storage = self._make_array(self._capacity)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if not 0 <= index <= self._size:
            raise IndexError()
        return self._storage[index]

    def _ensure_capacity(self):
        if self._size == self._capacity:
            self._resize( 2 * self._capacity )

    def _resize(self, new_capacity):
        new_storage = self._make_array(new_capacity)
        for index in range(self._size):
            new_storage[index] = self._storage[index]
        self._storage = new_storage
        self._capacity = new_capacity

    def _make_array(self, capacity):
        return ( capacity * ctypes.py_object)()