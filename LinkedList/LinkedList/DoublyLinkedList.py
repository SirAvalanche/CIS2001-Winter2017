class _Node:
    def __init__(self, value, next = None, previous = None):
        self.Value = value
        self.Next = next
        self.Previous = previous

class DoublyLinkedList():
    def __init__(self):
        self._head = _Node(None)
        self._head.Previous = self._head
        self._head.Next = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def IsEmpty(self):
        return self._size == 0

    def Add(self, item, index = None):
        if index == None:
            new_node = _Node(item, self._head, self._head.Previous)
            self._head.Previous = new_node
            new_node.Previous.Next = new_node
        
        elif index > self._size or index < 0:
            raise IndexError()
        
        else:
            current_node = self._head
            for current_index in range(index):
                current_node = current_node.Next

            new_node = _Node(item,current_node.Next, current_node)
            new_node.Previous.Next = new_node
            new_node.Next.Previous = new_node

        self._size += 1

    def Get(self, index):
        if index >= self._size or index < 0:
            raise IndexError()

        current_node = self._head.Next
        for current_index in range(index):
            current_node = current_node.Next
        return current_node.Value


list = DoublyLinkedList()

list.Add(10)
list.Add(20)
list.Add(30)
list.Add(25,2)
list.Add(5,0)
list.Add(40, 5)

for index in range(len(list)):
    print(list.Get(index))