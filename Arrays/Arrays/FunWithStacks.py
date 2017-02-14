from Stack import Stack
from Queue import Queue

my_scores = Stack()

my_scores.push(100)
my_scores.push(90)
my_scores.push(80)
my_scores.push(70)


while len(my_scores) > 0:
    print( my_scores.pop() )



def is_matched(expression):
    left = '({['
    right = ')}]'
    braces = Stack()
    for character in expression:
        if character in left:
            braces.push(character)
        elif character in right:
            if len(braces) == 0:
                return False
            if right.index(character) != left.index(braces.pop()):
                return False
    return len(braces) == 0

print(is_matched("self._storage[len(sel{f._stor}age) - 1]") )

line = Queue()
line.enqueue("Robert")
line.enqueue("Fatemeh")
print(line.dequeue())
line.enqueue("Susan")
line.enqueue("Mike")
print(line.dequeue())
print(line.dequeue())
line.enqueue("Aya")

while len(line) > 0:
    print(line.dequeue())
