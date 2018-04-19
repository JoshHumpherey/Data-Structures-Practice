# Script to test the implementation of my Stack
from Stack import Stack

myStack = Stack()
i = 0
while i < 10:
    myStack.push(i)
    i = i + 1

i = 0
while i < 11:
    poppedVar = myStack.pop()
    print(poppedVar)
    i = i + 1

input()
