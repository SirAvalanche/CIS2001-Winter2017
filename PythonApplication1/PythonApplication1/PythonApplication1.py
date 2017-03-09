from Stack import Stack
from Queue import Queue
import math

def IsPrime(n):
    if n < 2:
        return False
    for factor in range(int(math.sqrt(n)) + 1, 1, -1):
        if n % factor == 0:
            return False
    return True


def quick_trick_block_stack( n ):
 stack_q = Stack()
 while(not IsPrime(n)):
    n -= 1
 while(n != 1):
    if IsPrime(n):
        stack_q.push(Queue())
    else:
        top = stack_q.top()
        top.enqueue(n)
    n -= 1
 return stack_q 

def unstack(stack):
 for lenght in range(len(stack)):
    print(stack.pop())

unstack(quick_trick_block_stack(20))