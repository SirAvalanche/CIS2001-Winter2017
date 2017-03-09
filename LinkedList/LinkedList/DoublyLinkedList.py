class _Node:
    def __init__(self, value):
        self.Value = value
        self.Next = None
        self.Previous = None

class DoublyLinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def Add(self, item, index):
        if index > self._size:
            raise IndexError()
        if index == 0:
            new_node = _Node(item)
            self._tail.Next = new_node
            new_node.Previous = self._tail
            self._tail = new_node
            self._size += 1
        elif index == self._size:
            self.Enqueue(item)
        else:
            current_node = self._head
            current_index = 1
            while current_index < index:
                current_node = current_node.Next
                current_index += 1
            new_node = _Node(item)
            new_node.Previous = current_node.Previous
            new_node.Next = current_node
            new_node.Previous.Next = new_node
            current_node.Previous = new_node
            self._size += 1
        


    def Enqueue(self, item):
        new_node = _Node(item)
        
        if self._size == 0:
            self._tail = new_node

        new_node.Next = self._head

        if self._head != None:
            self._head.Previous = new_node

        self._head = new_node
        self._size += 1

    def First(self):
        return self._tail.Value

    def DeQueue(self):
        value = self._tail.Value
        self._tail = self._tail.Previous

        self._size -= 1
        return value

list = DoublyLinkedList()
list.Enqueue(10)
list.Enqueue(20)
list.Enqueue(30)
list.Add(25, 3)
list.Add(5,0)


while len(list) != 0:
    print(list.DeQueue())