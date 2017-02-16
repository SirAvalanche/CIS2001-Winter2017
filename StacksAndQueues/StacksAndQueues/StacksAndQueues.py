import math
from Stack import Stack
from Queue import Queue

def IsPrime(number):
    if number <= 1:
        return False
    for divsor in range(2,int(math.sqrt(number)) + 1):
        if number % divsor == 0:
            return False
    return True    

stack = Stack()
queue = Queue()

for number in range(10):
    if IsPrime(number):
        stack.push(number)
    else:
        queue.enqueue(number)

print(stack)
print(queue)

while len(stack) > 0:
    queue.enqueue(stack.pop())

while len(queue) > 0:
    print( queue.dequeue() )