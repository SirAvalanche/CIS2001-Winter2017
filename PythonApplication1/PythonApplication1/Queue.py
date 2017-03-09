class Queue():
    """description of class"""

    def __init__(self):
        self._storage = [None] * 10
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def IsEmpty(self):
        return self._size == 0

    def enqueue(self, obj):
        if self._size == len(self._storage):
            self._resize( 2 * self._size )
        self._storage[ ( self._size + self._front ) % len(self._storage) ] = obj
        self._size += 1

    def dequeue(self):
        if self.IsEmpty():
            raise IndexError("Queue is empty")
        value = self._storage[ self._front ]
        self._storage[ self._front ] = None
        self._front = ( self._front + 1 ) % len(self._storage )
        self._size -= 1
        return value

    def front(self):
        return self._storage[ self._front ]
    
    def __str__(self):
        return str(self._storage)

    def _resize(self, new_size ):
        temp = [None] * new_size
        for index in range( self._size ):
            temp[index] = self._storage[self._front]
            self._storage[ self._front ] = None
            self._front = ( self._front + 1 ) % len(self._storage)
        self._front = 0
        self._storage = temp
