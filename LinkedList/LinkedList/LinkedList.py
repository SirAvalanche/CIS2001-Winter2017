class _Node:
    def __init__(self, value):
        self.Value = value
        self.Next = None

class SinglyLinkedList():
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    # don't use add to back because it's O(N) performant

    #def Add_To_Back(self, item):
    #    if self._size == 0:
    #        self._head = Node(item)
    #    else:
    #        current_node = self._head
    #        while current_node.Next != None:
    #            current_node = current_node.Next
    #        current_node.Next = Node(item)
    #    self._size += 1

    def Push(self, item):
        new_node = _Node(item)
        new_node.Next = self._head
        self._head = new_node
        self._size += 1

    def Peek(self):
        return self._head.Value

    def Pop(self):
        value = self._head.Value
        self._head = self._head.Next
        self._size -= 1
        return value

list = SinglyLinkedList()
list.Push(10)
list.Push(20)
list.Push(30)

while len(list) != 0:
    print(list.Pop())

#first = Node(10)
#second = Node(20)

#first.Next = second

#third = Node(30)

#second.Next = third

#current_node = first
#while current_node.Next != None:
#    print(current_node.Value)
#    current_node = current_node.Next
#else:
#    print(current_node.Value)