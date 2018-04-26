from Stack import Stack
from Queue import Queue
import unittest


class StackTests(unittest.TestCase):

    def test_Push_Pop_Stack(self):
        expectedResult = 3
        testStack = Stack()
        testStack.Push(1)
        testStack.Push(2)
        testStack.Push(3)
        testResult = testStack.Pop()
        self.assertEqual(testResult, expectedResult)

    def test_StackSize(self):
        expectedResult = 3
        testStack = Stack()
        testStack.Push(1)
        testStack.Push(2)
        testStack.Push(3)
        testResult = testStack.Size()
        self.assertEqual(testResult,expectedResult)

class QueueTests(unittest.TestCase):

    def test_Enqueue_And_Dequeue(self):
        expectedResult = 1
        testQueue = Queue()
        testQueue.Enqueue(1)
        testQueue.Enqueue(2)
        testQueue.Enqueue(3)
        testResult = testQueue.Dequeue()
        self.assertEqual(expectedResult,testResult)

    def test_Empty_And_Size(self):
        expectedSize = 3
        testQueue = Queue()
        testQueue.Enqueue(1)
        testQueue.Enqueue(2)
        testQueue.Enqueue(3)
        testSize = testQueue.Size()
        self.assertEqual(testSize,expectedSize)
        isEmpty = testQueue.IsEmpty()
        self.assertEqual(isEmpty,False)
        testQueue.Dequeue()
        testQueue.Dequeue()
        testQueue.Dequeue()
        isEmpty = testQueue.IsEmpty()
        self.assertEqual(isEmpty,True)



if __name__ == '__main__':
    unittest.main()
